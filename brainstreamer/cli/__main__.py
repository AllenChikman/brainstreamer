import json

import click
import requests


@click.group()
def cli():
    pass


def send_get_request(host, port, directory):
    url = f'http://{host}:{port}/{directory}'
    r = requests.get(url=url)
    result = r.json()
    return json.dumps(result, indent=4)


@cli.command()
@click.option('-h', '--host', default='127.0.0.1')
@click.option('-p', '--port', default='5000')
def get_users(host, port):
    print(send_get_request(host, port, 'users'))


@cli.command()
@click.option('-h', '--host', default='127.0.0.1')
@click.option('-p', '--port', default='5000')
@click.argument('user_id')
def get_user(host, port, user_id):
    print(send_get_request(host, port, f'users/{user_id}'))


@cli.command()
@click.option('-h', '--host', default='127.0.0.1')
@click.option('-p', '--port', default='5000')
@click.argument('user_id')
def get_snapshots(host, port, user_id):
    print(send_get_request(host, port, f'users/{user_id}/snapshots'))


@cli.command()
@click.option('-h', '--host', default='127.0.0.1')
@click.option('-p', '--port', default='5000')
@click.argument('user_id')
@click.argument('snapshot_id')
def get_snapshot(host, port, user_id, snapshot_id):
    print(send_get_request(host, port, f'users/{user_id}/snapshots/{snapshot_id}'))


@cli.command()
@click.option('-h', '--host', default='127.0.0.1')
@click.option('-p', '--port', default='5000')
@click.option('-s', '--save', default='')
@click.argument('user_id')
@click.argument('snapshot_id')
@click.argument('result_name')
def get_result(host, port, save, user_id, snapshot_id, result_name):
    result = send_get_request(host, port, f'users/{user_id}/snapshots/{snapshot_id}/{result_name}')
    if save:
        with open(save, 'w+') as f:
            f.write(result)
    else:
        print(result)


if __name__ == '__main__':
    cli(prog_name='cli')
