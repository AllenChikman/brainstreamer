import sys
import importlib
import json
from pathlib import Path
from threading import Thread

from mindreader.drivers import MessageQueue


available_parsers = {}


def parse(parser_name, raw_data):
    return available_parsers[parser_name](raw_data)


def run_parser(parser_name, mq_url):
    mq = MessageQueue(mq_url)

    def handler(snapshot):
        result = parse(parser_name, snapshot)
        wrapped = wrap_parser_data(parser_name, result, snapshot)
        print(f"Parsed {parser_name}")
        mq.publish(parser_name, wrapped)

    mq.consume('snapshot', handler)


def wrap_parser_data(data_type, data, snapshot):
    snapshot = json.loads(snapshot)
    data = json.loads(data)
    wrapped = {'snapshot_id': snapshot['snapshot_id'],
               'results': {data_type: data}}
    return json.dumps(wrapped)


def run_all_parsers(mq_url):
    for parser_name in get_available_parsers():
        t = Thread(target=run_parser, args=(parser_name, mq_url))
        t.start()
        print(f'Parser {parser_name} is activated')


def get_available_parsers():
    return list(available_parsers.keys())


def load_parsers():
    root = Path("mindreader/parsers").absolute()
    sys.path.insert(0, str(root.parent))
    for file in root.iterdir():
        if file.name.startswith('_') or file.name == 'parsers.py' or not file.suffix == '.py':
            continue
        module = importlib.import_module(f'{root.name}.{file.stem}', package=root.name)
        for key, func in module.__dict__.items():
            if callable(func) and func.__name__.startswith("parse"):
                available_parsers[func.field] = func


load_parsers()
