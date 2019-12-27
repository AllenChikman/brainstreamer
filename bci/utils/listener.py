from .connection import Connection
import socket


class Listener:
    def __init__(self, port, host='0.0.0.0', backlog=1000, reuseaddr=True):
        self.port = port
        self.host = host
        self.backlog = backlog
        self.reuseaddr = reuseaddr
        self.server = socket.socket()

    def __repr__(self):
        return f'Listener(port={self.port!r}, host={self.host!r},' \
               f' backlog={self.backlog!r}, reuseaddr={self.reuseaddr!r})'

    def start(self):
        if self.reuseaddr:
            self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.server.bind((self.host, self.port))
        self.server.listen(self.backlog)

    def stop(self):
        self.server.close()

    def accept(self):
        client_sock, address = self.server.accept()
        return Connection(client_sock)

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()
