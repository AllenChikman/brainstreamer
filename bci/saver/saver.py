import json
from threading import Thread

from mindreader.drivers import Database, MessageQueue
from mindreader.parsers import get_available_parsers


class Saver:  # TODO: remove prints
    def __init__(self, database_url):
        self.db = Database(database_url)

    def save(self, topic, data):
        print(f'Now saving {topic}')
        data = json.loads(data)  # we expect data in JSON format
        if topic == 'user':
            self.db.insert_user(data)
        else:
            self.db.insert_data(data)

    def run_saver(self, parser_name, mq_url):
        mq = MessageQueue(mq_url)
        mq.consume(parser_name, lambda data: self.save(parser_name, data))

    def run_all_savers(self, mq_url):
        for parser_name in [*get_available_parsers(), 'user', 'snapshot_md']:
            t = Thread(target=self.run_saver, args=(parser_name, mq_url))
            t.start()
            print(f'Now listening on exchange: {parser_name}')

