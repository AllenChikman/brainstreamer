import click
from . import server
from ..utils import my_util_functions as my_utils


@click.group()
def cli():
    pass


@cli.command()
@click.option('-h', '--host', default='127.0.0.1', help="Server host")
@click.option('-p', '--port', default='8000',      help="Server port")
@click.argument('mq_url')
def run_server(host , port, mq_url):
    try:
        server.run(host, port, mq_url)
    except KeyboardInterrupt:
        print('Server terminated by user (KeyboardInterrupt)')


if __name__ == '__main__':
    my_utils.init_logger("server")
    cli(prog_name='brainstreamer')
