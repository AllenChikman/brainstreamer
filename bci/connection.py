import socket


class Connection:
    def __init__(self, sock):
        self.sock = sock

    def __repr__(self):
        sock = self.sock.getsockname()
        peer = self.sock.getpeername()
        return f'<Connection from {sock[0]}:{sock[1]} to {peer[0]}:{peer[1]}>'

    def send(self, data):
        self.sock.sendall(data)

    def receive(self, size):
        chunks = []
        while size > 0:
            chunk = self.sock.recv(size)
            if not chunk:
                raise RuntimeError('incomplete data')
            chunks.append(chunk)
            size -= len(chunk)
        return b''.join(chunks)

    def close(self):
        self.sock.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sock.close()

    @classmethod
    def connect(cls, host, port):
        conn = socket.socket()
        conn.connect((host, port))
        return Connection(conn)
