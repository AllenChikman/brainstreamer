import click
from . import parse as parse_data
from . import run_parser as activate_parser
from .parsing_manager import run_all_parsers
from ..utils import my_util_functions as my_utils


DEFAULT_MQ_ADDRESS = "rabbitmq://127.0.0.1:5672"

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
@click.argument('mq_url')
def run_parser(parser_name, mq_url):
    activate_parser(parser_name, mq_url)


@cli.command()
def run_parsers():
    run_all_parsers(DEFAULT_MQ_ADDRESS)


if __name__ == '__main__':
    import logging
    my_utils.init_logger("parsers")
    logger = logging.getLogger(__name__)
    logger.debug("parsing")
    cli(prog_name='parsers')
