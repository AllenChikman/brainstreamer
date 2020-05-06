import json
import logging
from threading import Thread

from brainstreamer.platforms.databases import DBWrapper
from brainstreamer.platforms.message_queue import MqWrapper
from brainstreamer.parsers import get_available_parsers


class Saver:
    def __init__(self, database_url):
        self.db = DBWrapper(database_url)
        self.logger = logging.getLogger(__name__)

    def save(self, topic, data):
        data = json.loads(data)
        if topic == 'user':
            self.db.insert_user(data)
        else:
            self.db.insert_results(data)

    def run_saver(self, topic, mq_url):
        mq = MqWrapper(mq_url)

        def handler(data):
            self.save(topic, data)

        mq.consume(topic, handler)

    def run_savers(self, mq_url):
        for parser_name in [*get_available_parsers(), 'user']:
            t = Thread(target=self.run_saver, args=(parser_name, mq_url))
            t.start()
