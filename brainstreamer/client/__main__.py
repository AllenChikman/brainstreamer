import click
from . import client
from ..utils import my_util_functions as my_utils


@click.group()
def cli():
    pass


@cli.command()
@click.option('--address', default="127.0.0.1:8000", help='address in a format of ip:port')
@click.option('--sample_path', default="./brainstreamer/data", help='path of the mind sample')
def upload_sample(address, sample_path):
    ip, port = address.split(":")
    formatted_address = (ip, int(port))
    try:
        client.run(formatted_address, sample_path)
    except Exception as error:
        print(f'ERROR: {error}')
    pass


if __name__ == '__main__':
    my_utils.init_logger("client")
    cli(prog_name='brainstreamer')
