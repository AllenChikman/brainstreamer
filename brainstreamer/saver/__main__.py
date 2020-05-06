import click
from . import Saver
from ..utils import my_util_functions as my_utils


@click.group()
def cli():
    pass


@cli.command()
@click.option('-d', '--database', default='mongodb://127.0.0.1:27017')
@click.argument('topic')
@click.argument('path')
def save(database, topic, path):
    saver = Saver(database)
    with open(path, 'r') as f:
        saver.save(topic, f.read())


@cli.command()
@click.option('-d', '--db_url', default='mongodb://127.0.0.1:27017')
@click.option('-m', '--mq_url', default='rabbitmq://127.0.0.1:5672')
def run_saver(db_url, mq_url):
    saver = Saver(db_url)
    saver.run_savers(mq_url)


if __name__ == '__main__':
    my_utils.init_logger("saver")
    cli(prog_name='saver')
