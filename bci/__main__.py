import click
from . import server, client
from .web import web


@click.group()
def cli():
    pass


@cli.command()
@click.option('--address', default="127.0.0.1:8000", help='address in a format of ip:port')
@click.option('--user', default=1, help='user id')
@click.option('--thought', help='your thought as a string')
def upload_thought(address, user, thought):
    ip, port = address.split(":")
    formatted_address = (ip, int(port))
    try:
        client.upload_thought(formatted_address, int(user), thought)
    except Exception as error:
        print(f'ERROR: {error}')


@cli.command()
@click.option('--address', default="127.0.0.1:8000", help='address in a format of ip:port')
@click.option('--data_dir', default=".", help='data dir')
def run_server(address, data_dir):
    host, port = address.split(':')
    formatted_address = (host, int(port))
    try:
        server.run_server(formatted_address, data_dir)
    except KeyboardInterrupt:
        print('Server terminated by user (KeyboardInterrupt)')


@cli.command()
@click.option('--address', default="127.0.0.1:8000", help='address in a format of ip:port')
@click.option('--data', default="./web/web_data", help='data dir')
def run_webserver(address, data_dir):
    ip, port = address.split(':')
    try:
        web.run_webserver((ip, port), data_dir)
    except Exception as error:
        print(f'ERROR: {error}')


if __name__ == '__main__':
    cli(prog_name='bci')

