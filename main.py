from common.client import command_client

import socket

PORT = 1414

def main():
    print(f"Server running on {socket.gethostbyname(socket.gethostname())}:{PORT}")
    while True:
        connection, address = s.accept()
        command_client.CommandClient(connection, address)

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    s.bind(("0.0.0.0", PORT))
    s.listen(socket.SOMAXCONN)

    main()
