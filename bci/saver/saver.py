import json
import logging
from threading import Thread


from bci.databases import Database
from bci.message_queue import MqWrapper
from bci.parsers import get_available_parsers


class Saver:
    def __init__(self, database_url):
        self.db = Database(database_url)
        self.logger = logging.getLogger(__name__)

    def save(self, topic, data):
        data = json.loads(data)
        if topic == 'user':
            print(f"user saved{data}")
            self.db.insert_user(data)
        else:
            self.db.insert_data(data)

    def run_saver(self, topic, mq_url):
        mq = MqWrapper(mq_url)

        def handler(data):
            self.save(topic, data)

        print(f'consuming on {mq_url} topic: {topic}')
        mq.consume(topic, handler)

    def run_all_savers(self, mq_url):
        for parser_name in [*get_available_parsers(), 'user']:
            t = Thread(target=self.run_saver, args=(parser_name, mq_url))
            t.start()
            print(f'Now listening on topic: {parser_name}')

