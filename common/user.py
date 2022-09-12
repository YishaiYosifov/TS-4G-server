from .commands import *
from . import *

import threading
import socket
import json

with open("config.json") as f: CONFIG = json.load(f)

class User(threading.Thread):
    users = {}

    def __init__(self, connection : socket.socket, address : tuple):
        threading.Thread.__init__(self)

        self.ip, self.id = address
        self.connection = connection

        print(f"{self.ip}:{self.id} connected")

        self.users[self.id] = self
        self.inputBlocked = False
        self.role = 0

        self.start()

    def run(self):
        while True:
            try: data = self.connection.recv(1024)
            except (ConnectionResetError, ConnectionAbortedError):
                self.disconnect()
                return

            if not data:
                self.disconnect()
                return

            data = data.decode("utf-8")
            try: data = json.loads(data)
            except json.JSONDecodeError:
                self.error(Errors.WRONG_DATA_TYPE, "Data must be a dict")
                continue

            if not isinstance(data, dict):
                self.error(Errors.WRONG_DATA_TYPE, "Data must be a dict")
                continue
            elif not "request_type" in data:
                self.error(Errors.MISSING_ARGUMENT, "Missing Required Argument: request_type")
                continue

            try: command = COMMANDS[data["request_type"]]
            except KeyError:
                self.error(Errors.INVALID_REQUEST_TYPE, f"Invalid Request Type: {data['request_type']}")
                continue

            if command.role > self.role:
                self.error(Errors.INSUFFICIENT_ROLE, f"Insufficient Permissions Level: {self.role}")
                continue
            
            arguments = []
            for argument in command.arguments:
                foundBadArgument = True

                value = None
                if argument.name in data:
                    value = data[argument.name]
                    if not isinstance(value, argument.type):
                        self.error(Errors.INVALID_TYPE, f"Argument {argument.name} must be type {argument.type.__name__}")
                        break

                    if not argument.validation(self, value): break
                elif argument.required:
                    self.error(Errors.MISSING_ARGUMENT, f"Missing Required Argument: {argument.name}")
                    break
                arguments.append(value)
                foundBadArgument = False

            if foundBadArgument: continue

            getattr(self, data["request_type"])(*arguments)
    
    def block_input(self, targetID):
        user = self.users[targetID]
        if user.inputBlocked:
            self.error(Errors.USER_ALREADY_AFFECTED, f"Input for user {targetID} already blocked")
            return
        user.inputBlocked = True

        user.action(Actions.BLOCK_INPUT)
    
    def unblock_input(self, targetID):
        user = self.users[targetID]
        if not user.inputBlocked:
            self.error(Errors.USER_NOT_AFFECTED, f"Input for user {targetID} is not blocked")
            return
        user.inputBlocked = False

        user.action(Actions.UNBLOCK_INPUT)
    
    def login(self, role : int, password : str):
        if not role in CONFIG["roles"]:
            self.error(Errors.INVALID_ROLE, f"Unknwon Role: {role}")
            return

        rolePassword = CONFIG["roles"][role]
        if rolePassword and password != rolePassword:
            self.error(Errors.INVALID_PASSWORD, "Invalid Password")
            return
        
        self.role = int(role)
        self.callback(Callbacks.LOGGED_IN_SUCCESSFULLY)
    
    def disconnect(self):
        print(f"{self.ip}:{self.id} disconnected")
        self.connection.close()
        self.users.pop(self.id)
    
    def error(self, type : str, msg : str): self.__send({"request_type": "error", "type": type, "msg": msg})
    def action(self, type : str): self.__send({"request_type": "action", "type": type})
    def callback(self, type : str, data : dict = {}): self.__send({"request_type": "callback", "type": type} | data)

    def __send(self, data : dict): self.connection.send(json.dumps(data).encode("utf-8"))