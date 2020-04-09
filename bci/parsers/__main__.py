import click
from . import parse as parse_data
from . import run_parser as register_parser
from .parsers import run_all_parsers


@click.group()
def cli():
    pass


@cli.command()
@click.argument('parser_name')
@click.argument('path')
def parse(parser_name, path):
    with open(path, 'r') as f:
        result = parse_data(parser_name, f.read())
    print(result)


@cli.command()
@click.argument('parser_name')
@click.option('--mq_url', default='rabbitmq://127.0.0.1:5672')
def run_parser(parser_name, mq_url):
    register_parser(parser_name, mq_url)


@cli.command()
def run_parsers():
    run_all_parsers('rabbitmq://127.0.0.1:5672')


if __name__ == '__main__':
    cli(prog_name='parsers')
