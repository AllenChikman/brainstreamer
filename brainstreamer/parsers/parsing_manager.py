from threading import Thread
import logging
import json

from ..utils import my_util_functions as my_utils
from brainstreamer.platforms.message_queue import MqWrapper

logger = logging.getLogger(__name__)
available_parsers = my_utils.load_drivers(drivers_path="./brainstreamer/parsers/parsing_drivers",
                                          driver_type="function")


# Just return the available parsers/drivers
def get_available_parsers():
    return list(available_parsers.keys())


# process the parsed data and wrap it with metadata for the saver
def _prepare_publish_data(topic, parsed_data, snapshot):
    snapshot_dict = json.loads(snapshot)

    datetime = snapshot_dict["datetime"]
    snapshot_id = snapshot_dict["snapshot_id"]
    user_id = snapshot_dict["user_id"]

    metadata = dict(datetime=datetime, snapshot_id=snapshot_id, user_id=user_id)
    prepared_data = dict(**metadata, results={topic: parsed_data})

    return json.dumps(prepared_data)


# Start listening on the MQ, with a handler that know to parse the snapshots
def run_parser(parser_name, mq_url):
    mq = MqWrapper(mq_url)

    def handler(snapshot):
        parsed_data = parse(parser_name, snapshot)
        print(f"Parsed {parser_name}")
        data = _prepare_publish_data(parser_name, parsed_data, snapshot)
        mq.publish(parser_name, data)

    mq.consume('snapshot', handler)


# Call to the proper parser (according to the given name) and ask
# him to parse the given data
def parse(parser_name, raw_data):
    return json.dumps(available_parsers[parser_name](raw_data))


# Activate a thread for each available parser driver
def run_all_parsers(mq_url):
    for parser_name in get_available_parsers():
        t = Thread(target=run_parser, args=(parser_name, mq_url))
        t.start()
        print(f'Parser {parser_name} is activated')
