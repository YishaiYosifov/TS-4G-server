from __future__ import annotations

import common.client.command_client as command_client
import threading
import socket
import struct
import time

class ScreenshareClient(threading.Thread):
    users : dict[int, ScreenshareClient] = {}

    def __init__(self, connection: socket.socket, address: tuple, targetID : int, screenshareID : int):
        threading.Thread.__init__(self)

        self.ip, self.id = address
        self.connection = connection

        self.users[targetID] = self
        self.screenshareID = screenshareID

        self.targetUser : command_client.CommandClient = None
        self.started = False

        self.start()
    
    def run(self):
        while not self.started:
            if self.connection.fileno() == -1:
                self.quit()
                return

            time.sleep(1)
        
        data = b""
        payloadSize = struct.calcsize("Q")
        while True:
            while len(data) < payloadSize:
                try: packet = self.targetUser.connection.recv(4096)
                except (ConnectionResetError, ConnectionAbortedError):
                    self.quit()
                    return

                if not packet:
                    self.quit()
                    return

                data += packet

            packedMessageSize = data[:payloadSize]
            data = data[payloadSize:]
            messageSize = struct.unpack("Q", packedMessageSize)[0]

            if messageSize > 2000000:
                self.quit()
                return
            
            try:
                while len(data) < messageSize: data += self.targetUser.connection.recv(4096)
            except (ConnectionError, OSError):
                self.quit()
                return

            frame = data[:messageSize]
            frame = struct.pack("Q", len(frame)) + frame
            try: self.connection.sendall(frame)
            except ConnectionResetError:
                self.quit()
                return

            data = data[messageSize:]
    
    def quit(self):
        if self.targetUser.connection.fileno() != -1:
            self.targetUser.connection.close()
            print(f"{self.targetUser.ip}:{self.targetUser.id} disconnected")

        if self.connection.fileno() != -1:
            self.connection.close()
            print(f"{self.ip}:{self.id} disconnected")
