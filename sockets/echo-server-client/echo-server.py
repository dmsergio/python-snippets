import socket


# HOST = "127.0.0.1"
HOST = ""
PORT = 65432


def main():
    # Create a new socket as a context manager (close the socket automatically)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as _socket:
        print(f"Server socket: {_socket!r}")

        # Associate the socket to a specific network interface (IP and port)
        _socket.bind((HOST, PORT))

        # Enables a server to accept connections
        _socket.listen()

        # Blocks the execution and waits for an incoming connection. When a
        # client connects, it returns a new socket object. This new socket is
        # different from initial socket, this one is the socket created with
        # the connection between server and client.
        conn, addr = _socket.accept()
        with conn:
            print(f"Socket between server and client: {conn!r}")
            print(f"Connected by {addr}")

            # Infinite loop to receive all data sent by client
            while True:
                data = conn.recv(1024)
                if not data:
                    break

                # Returns the data received to the client again
                conn.sendall(data)


if __name__ == "__main__":
    main()
