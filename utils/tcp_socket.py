import socket

class TcpSocket:

  def __init__(self, host = "0.0.0.0", port = 8001) -> None:

    # Create socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # This is for linux and allows the socket to be reused
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind host and port to the socket
    server.bind((host, port))

    # Listen (1) specifies the number of unaccepted connections 
    # that the system will allow before refusing new connections
    server.listen(1)

    # Show the user this server is listening
    print(f'Listening on {host}:{port}')

    self.server = server
