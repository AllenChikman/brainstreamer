import json
import logging
from threading import Thread

from brainstreamer.platforms.databases import DBWrapper
from brainstreamer.platforms.message_queue import MqWrapper
from brainstreamer.parsers import get_available_parsers


# The Saver class listens on the given MQ and consumes parsed data, \
# and afterwards, saves that data to a given DB
class Saver:
    def __init__(self, database_url):
        self.db = DBWrapper(database_url)
        self.logger = logging.getLogger(__name__)

    # Saves the parsed data to the DB according to the provided topic
    def save(self, topic, data):
        data = json.loads(data)

        # There is a distinction between user data and other parsed data
        if topic == 'user':
            self.db.insert_user(data)
        else:
            self.db.insert_results(data)

    # Consumes from the MQ on the given topic with the a "save" handler
    def run_saver(self, topic, mq_url):
        mq = MqWrapper(mq_url)

        def handler(data):
            self.save(topic, data)

        mq.consume(topic, handler)

    # This function open a thread for each expected data topic, which consumes on the MQ.
    def run_savers(self, mq_url):
        for parser_name in [*get_available_parsers(), 'user']:
            t = Thread(target=self.run_saver, args=(parser_name, mq_url))
            t.start()
