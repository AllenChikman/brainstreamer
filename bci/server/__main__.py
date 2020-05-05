import click
from . import server
from ..utils import my_util_functions as my_utils


@click.group()
def cli():
    pass


@cli.command()
@click.option('--address', default="127.0.0.1:8000", help='address in a format of ip:port')
def run_server(address):
    host, port = address.split(':')
    formatted_address = (host, int(port))
    try:
        server.run(formatted_address)
    except KeyboardInterrupt:
        print('Server terminated by user (KeyboardInterrupt)')


if __name__ == '__main__':
    my_utils.init_logger("server")
    cli(prog_name='bci')
