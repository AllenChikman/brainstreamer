import click
from . import run_website


@click.group()
def cli():
    pass

@cli.command()
@click.option('-h', '--host',      default='127.0.0.1'  , help="server host")
@click.option('-p', '--port',      default='8080'       , help="server port")
@click.option('-H', '--api-host',  default='127.0.0.1'  , help="API Host")
@click.option('-P', '--api-port',  default='5000'       , help="API port")
def run_server(server_host, server_port, api_host, api_port):
    formatted_api_address = f"http://{api_host}:{api_port}";
    try:
        run_website(server_host, server_port,formatted_api_address)
    except Exception as error:
        print(f'GUI ERROR: {error}')
        return 1

if __name__ == '__main__':
    cli(prog_name='gui')
