import click
from . import run_website


@click.group()
def cli():
    pass


@cli.command()
@click.option('-h', '--host', default='127.0.0.1', help="server host")
@click.option('-p', '--port', default='8080', help="server port")
def run_server(host, port):
    try:
        run_website(host, port)
    except Exception as error:
        print(f'GUI ERROR: {error}')
        return 1

if __name__ == '__main__':
    cli(prog_name='gui')
