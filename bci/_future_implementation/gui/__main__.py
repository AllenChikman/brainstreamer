import click
from . import run_server as run


@click.group()
def cli():
    pass


@cli.command()
@click.option('-h', '--host', default='127.0.0.1')
@click.option('-p', '--port', default='8080')
@click.option('-H', '--api-host', default='127.0.0.1')
@click.option('-P', '--api-port', default='5000')
def run_server(host, port, api_host, api_port):
    run(host, port, api_host, api_port)


if __name__ == '__main__':
    cli(prog_name='api')
