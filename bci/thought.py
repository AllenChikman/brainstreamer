import struct
from datetime import datetime


class Thought:
    """Represents a thought of a user"""
    def __init__(self, user_id, timestamp, thought):
        self.user_id = user_id
        self.timestamp = timestamp
        self.thought = thought

    def __repr__(self):
        return f'Thought(user_id={self.user_id!r}, timestamp={self.timestamp!r}, thought={self.thought!r})'

    def __str__(self):
        return f'[{self.timestamp}] user {self.user_id}: {self.thought}'

    def __eq__(self, other):
        return isinstance(other, Thought) and self.user_id == other.user_id \
               and self.timestamp == other.timestamp and self.thought == other.thought

    def serialize(self):
        user_bytes = struct.pack('Q', self.user_id)
        timestamp_bytes = struct.pack('Q', int(datetime.timestamp(self.timestamp)))
        msg_len_bytes = struct.pack('I', len(self.thought))
        msg_bytes = self.thought.encode('utf8')
        return user_bytes + timestamp_bytes + msg_len_bytes + msg_bytes

    @staticmethod
    def deserialize(data):
        user_id = struct.unpack('Q', data[0:8])[0]
        timestamp = struct.unpack('Q', data[8:16])[0]
        n = struct.unpack('I', data[16:20])[0]
        thought = data[20:20+n].decode('utf8')
        timestamp = datetime.fromtimestamp(timestamp)
        return Thought(user_id, timestamp, thought)
