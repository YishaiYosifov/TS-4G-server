from __future__ import annotations

from common.commands.functions import commandFunctions
from common.request_constants import *
from common.commands import COMMANDS

import common.client.screenshare_client as screenshare_client
import threading
import socket
import json

class CommandClient(threading.Thread):
    users : dict[int, CommandClient] = {}

    def __init__(self, connection : socket.socket, address : tuple):
        threading.Thread.__init__(self)

        self.ip, self.id = address
        self.connection = connection

        print(f"{self.ip}:{self.id} connected")

        self.users[self.id] = self

        self.inputBlocked = False
        self.screenBlocked = False

        self.screenshare  : int = None
        self.role : int = None
        self.pcName : str = None

        self.closed = False
        self.start()

    def run(self):
        while True:
            if self.closed: return

            try: data = self.connection.recv(1024)
            except (ConnectionResetError, ConnectionAbortedError):
                self.disconnect()
                return

            if not data:
                self.disconnect()
                return

            for request in data.split(b"}{"):
                if not request: continue

                if not request.endswith(b"}"): request += b"}"
                elif not request.startswith(b"{"): request = b"{" + request

                try:
                    request = request.decode("utf-8")
                    request = json.loads(request)
                except (json.JSONDecodeError, UnicodeDecodeError):
                    self.error(Errors.WRONG_DATA_TYPE, "Data must be a dict")
                    continue

                if not isinstance(request, dict):
                    self.error(Errors.WRONG_DATA_TYPE, "Data must be a dict")
                    continue
                elif not "request_type" in request:
                    self.error(Errors.MISSING_ARGUMENT, "Missing Required Argument: request_type")
                    continue

                try: command = COMMANDS[request["request_type"]]
                except KeyError:
                    self.error(Errors.INVALID_REQUEST_TYPE, f"Invalid Request Type: {request['request_type']}")
                    continue
                
                if not command.role is None:
                    if not self.role:
                        self.error(Errors.INSUFFICIENT_ROLE, "Not Logged in")
                        continue
                    elif command.role != self.role:
                        self.error(Errors.INSUFFICIENT_ROLE, f"Insufficient Permissions Level: {self.role}")
                        continue
                
                arguments = []
                foundBadArgument = False
                for argument in command.arguments:
                    foundBadArgument = True

                    value = None
                    if argument.name in request:
                        value = request[argument.name]
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

                arguments.insert(0, self)
                commandFunctions[request["request_type"]](*arguments)
    
    def disconnect(self):
        print(f"{self.ip}:{self.id} disconnected")

        try: screenshare_client.ScreenshareClient.users[self.id].quit()
        except KeyError: pass
        
        CommandClient.callback_to_all(Callbacks.USER_DISCONNECTED, data={"user": self.to_dict()}, exclude=[self.id])

        self.connection.close()
        self.users.pop(self.id)

    def to_dict(self) -> dict: return {"id": self.id, "pc_name": self.pcName, "blocked": {"screen": self.screenBlocked, "input": self.inputBlocked}}

    def error(self, type : str, msg : str): self.__send({"request_type": "error", "type": type, "msg": msg})
    def action(self, type : str, data : dict = {}): self.__send({"request_type": "action", "type": type} | data)
    def callback(self, type : str, data : dict = {}): self.__send({"request_type": "callback", "type": type} | data)

    def __send(self, data : dict):
        try: self.connection.sendall((json.dumps(data) + "\r").encode("utf-8"))
        except ConnectionResetError: pass

    @staticmethod
    def __send_to_all(data : dict, exclude : list = []):
        for user in CommandClient.users.values():
            if user.id in exclude: continue
            try: user.__send(data)
            except OSError: pass
    
    @staticmethod
    def callback_to_all(type : str, data : dict, exclude : list = []): CommandClient.__send_to_all({"request_type": "callback", "type": type} | data, exclude)