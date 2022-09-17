import threading
import socket
import struct
import time

class ScreenshareClient(threading.Thread):
    users = {}

    def __init__(self, connection: socket.socket, address: tuple, targetID : int, screenshareID : int):
        threading.Thread.__init__(self)

        self.ip, self.id = address
        self.connection = connection

        self.users[targetID] = self
        self.screenshareID = screenshareID

        self.target = None
        self.started = False

        self.start()
    
    def run(self):
        self.connection.setblocking(0)
        while not self.started:
            try:
                data = self.connection.recv(16, socket.MSG_PEEK)
                if not data:
                    self.quit()
                    return
            except (ConnectionResetError, BlockingIOError) as e:
                if not isinstance(e, BlockingIOError):
                    self.quit()
                    return

            time.sleep(1)
        self.connection.setblocking(1)
        
        data = b""
        payloadSize = struct.calcsize("Q")
        while True:
            while len(data) < payloadSize:
                try: packet = self.target.recv(4096)
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
                while len(data) < messageSize: data += self.target.recv(4*1024)
            except ConnectionError:
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
        try: self.target.close()
        except AttributeError: pass
        self.connection.close()
