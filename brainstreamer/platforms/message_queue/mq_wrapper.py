import logging

from furl import furl
from brainstreamer.utils import my_util_functions as my_utils

logger = logging.getLogger(__name__)
mq_drivers = my_utils.load_drivers(drivers_path="./brainstreamer/platforms/message_queue/mq_drivers", driver_type="class")


class MqWrapper:

    def __init__(self, url):
        url = furl(url)
        scheme, host, port = url.scheme, url.host, url.port
        logger.debug(f"Init of Mq: {url}")

        if scheme not in mq_drivers:
            raise ValueError(f"Unsupported MQ driver: {scheme}")
        try:
            self.mq = mq_drivers[scheme](host, port)
        except ConnectionError:
            raise ConnectionError(f"Couldn't connect to MQ driver: {scheme}{mq_drivers}{host}{port}")

    def publish(self, topic, message):
        self.mq.publish(topic, message)

    def consume(self, topic, handler):
        self.mq.consume(topic, handler)

    def __repr__(self):
        return self.mq.__repr__()
