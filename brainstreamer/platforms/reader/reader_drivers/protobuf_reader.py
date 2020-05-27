import gzip
import struct
from brainstreamer.platforms.protocols.protocol_drivers.client_server_protobuf import User, Snapshot

UINT_SIZE = 4


# This is a reader of protobuf type
class ProtoReader:
    scheme = 'protobuf'

    def __init__(self, path):
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
        return user

    def get_snapshot(self):
        snapshot = Snapshot()
        try:
            snapshot.ParseFromString(self._get_data())
            return snapshot
        except struct.error:
            return None
