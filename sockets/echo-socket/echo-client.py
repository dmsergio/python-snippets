import socket


HOST = "127.0.0.1"  # server hostname or IP
PORT = 65432  # port used by the server


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as _socket:
        print(f"Client socket: {_socket!r}")

        # Client socket connects to the server
        _socket.connect((HOST, PORT))

        # Client sends data to the server
        _socket.sendall(b"Hello, world")

        # Client receives data from the server
        data = _socket.recv(1024)

    print(f"Received {data!r}")


if __name__ == "__main__":
    main()
