import gzip
import struct
import logging
from .data.cortex_pb2 import User, Snapshot

UINT_SIZE = 4


class ProtoReader:
    def __init__(self, path):
        self.logger = logging.getLogger(__name__)
        self.path = path
        self.stream = gzip.open(path, "rb")

    def _get_data(self):
        size_str = self.stream.read(UINT_SIZE)
        size_int, = struct.unpack('I', size_str)
        data = self.stream.read(size_int)
        return data

    def get_user(self):
        user = User()
        user.ParseFromString(self._get_data())
        self.logger.debug(f"username: {user.username}")
        return user

    def get_snapshot(self):
        snapshot = Snapshot()
        snapshot.ParseFromString(self._get_data())
        return snapshot


class Reader:
    def __init__(self, path, file_reader=ProtoReader):
        self.path = path
        self.file_reader = file_reader(path)

        self.logger = logging.getLogger(__name__)
        self.logger.debug("Reader initialized")

    def get_user(self):
        self.logger.debug("getting user")
        return self.file_reader.get_user()

    def get_snapshot(self):
        self.logger.debug("getting snapshot")
        return self.file_reader.get_snapshot()

    def close(self):
        self.file_reader.stream.close()

    def __repr__(self):
        return f'Reader(path={self.path})'

    def __str__(self):
        return f'Reader(path={self.path})'

    def __iter__(self):
        while snapshot := self.file_reader.get_snapshot():
            yield snapshot
