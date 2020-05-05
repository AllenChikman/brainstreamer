import sys
import importlib
import json
from pathlib import Path
from threading import Thread
import logging

from bci.message_queue import MqWrapper

logger = logging.getLogger(__name__)

available_parsers = {}


def get_available_parsers():
    return list(available_parsers.keys())


# API

def parse(parser_name, raw_data):
    return available_parsers[parser_name](raw_data)


def run_parser(parser_name, mq_url):
    mq = MqWrapper(mq_url)

    def handler(snapshot):
        parsed_data = parse(parser_name, snapshot)
        print(f"Parsed {parser_name}")
        data = prepare_publish_data(parser_name, parsed_data, snapshot)
        mq.publish(parser_name, data)

    mq.consume('snapshot', handler)


def prepare_publish_data(topic, parsed_data, snapshot):
    snapshot_dict = json.loads(snapshot)

    datetime = snapshot_dict['datetime']
    snapshot_id = snapshot_dict['snapshot_id']
    user_id = snapshot_dict['user_id']

    metadata = dict(datetime=datetime, snapshot_id=snapshot_id, user_id=user_id)

    prepared_data = dict(**metadata, results={topic: parsed_data})

    return json.dumps(prepared_data)


def run_all_parsers(mq_url):
    for parser_name in get_available_parsers():
        t = Thread(target=run_parser, args=(parser_name, mq_url))
        t.start()
        print(f'Parser {parser_name} is activated')


def load_parsers():
    root = Path("bci/parsers/workers").absolute()
    sys.path.insert(0, str(root.parent))
    for file in root.iterdir():
        if file.name.startswith('_') or file.name == 'parsers.py' or not file.suffix == '.py':
            continue

        module = importlib.import_module(f'{root.name}.{file.stem}', package=root.name)
        for key, func in module.__dict__.items():
            if callable(func) and func.__name__.startswith("parse"):
                available_parsers[func.topic] = func


load_parsers()
