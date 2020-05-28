import click
from . import client
from ..utils import my_util_functions as my_utils


@click.group()
def cli():
    pass


@cli.command()
@click.option('-h', '--host', default='127.0.0.1',      help="Server host")
@click.option('-p', '--port', default=8000,             help="Server port")
@click.option('-n', '--num-snaps', default=0,           help="Number of snapshots to read")
@click.argument('path')
def upload_sample(host, port , num_snaps, path):
    try:
        client.upload_sample(host, int(port), int(num_snaps) , path)
    except Exception as error:
        print(f'ERROR: {error}')
    pass


if __name__ == '__main__':
    my_utils.init_logger("client")
    cli(prog_name='brainstreamer')
