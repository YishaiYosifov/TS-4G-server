from .util import REQUEST_TYPES, Errors

import socket
import json

class User:
    users = {}

    def __init__(self, connection : socket.socket, address : tuple):
        self.ip, self.id = address
        self.connection = connection

        print(f"{self.ip}:{self.id} connected")

        self.users[self.id] = self

    def mainloop(self):
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
                self.error(Errors.WRONG_DATA_TYPE, "Data must be dict")
                continue

            if not isinstance(data, dict):
                self.error(Errors.WRONG_DATA_TYPE, "Data must be dict")
                continue
            elif not "request_type" in data:
                self.error(Errors.MISSING_ARGUMENT, "Missing Required Argument: request_type")
                continue

            try: requiredArguments = REQUEST_TYPES[data["request_type"]]
            except KeyError:
                self.error(Errors.INVALID_REQUEST_TYPE, f"Invalid Request Type: {data['request_type']}")
                continue
            
            def check_arguments() -> bool:
                for requiredArgument, requiredType in requiredArguments.items():
                    checkArgument = requiredArgument.removeprefix("_")

                    if not requiredArgument.startswith("_") and not checkArgument in data:
                        self.error(Errors.MISSING_ARGUMENT, f"Missing Required Argument: {requiredArgument}")
                        return False
                    elif not isinstance(data[checkArgument], requiredType):
                        self.error(Errors.INVALID_TYPE, f"Argument {checkArgument} must be type {requiredType.__name__}")
                        return False
                return True

            if not check_arguments(): continue

    def disconnect(self):
        print(f"{self.ip}:{self.id} disconnected")
        self.connection.close()
        self.users.pop(self.id)
    
    def error(self, type, msg):
        self.connection.send(json.dumps({"request_type": "error", "type": type, "msg": msg}).encode("utf-8"))