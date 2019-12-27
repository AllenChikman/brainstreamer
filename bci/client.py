from .thought import Thought
from .utils.connection import Connection
import datetime as dt
import click


@click.command()
@click.option('--address', default="127.0.0.1:8000", help='address in a format of ip:port')
@click.option('--user', default=1, help='user id')
@click.option('--thought', help='your thought as a string')
def upload_thought(address_tup, user, thought):
    conn = Connection.connect(*address_tup)

    with conn:
        thought = Thought(user, dt.datetime.now(), thought)
        conn.send(thought.serialize())


if __name__ == '__main__':
    upload_thought()
