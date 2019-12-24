from .thought import Thought
from .utils.connection import Connection
import datetime as dt


def upload_thought(address, user, thought):

    conn = Connection.connect(*address)

    with conn:
        thought = Thought(user, dt.datetime.now(), thought)
        conn.send(thought.serialize())
