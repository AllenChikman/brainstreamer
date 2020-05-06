import struct
import io
from brainstreamer.platforms.protocols import User, Snapshot

"""
protocol will include passing data of the user and single snapshot of his in the following manner:
UINT representing the size of the user data, following with that amount of user data, and then similarly
UINT representing the size of the user's snapshot, following with that amount of snapshot data.
( user length , user data, snapshot_len , snapshot data)   
"""


def serialize_message(user, snapshot):
    user_data = user.SerializeToString()
    user_len = struct.pack('I', len(user_data))

    snapshot_data = snapshot.SerializeToString()
    snapshot_len = struct.pack('I', len(snapshot_data))

    serialized_msg = user_len + user_data + snapshot_len + snapshot_data
    return serialized_msg


def deserialize_message(message_bytes):
    stream = io.BytesIO(message_bytes)

    user = User()
    user_len, = struct.unpack('I', stream.read(4))
    user_bytes = stream.read(user_len)
    user.ParseFromString(user_bytes)

    snapshot = Snapshot()
    snapshot_len, = struct.unpack('I', stream.read(4))
    snapshot_bytes = stream.read(snapshot_len)
    snapshot.ParseFromString(snapshot_bytes)

    return user, snapshot
