import pika
import logging

from furl import furl

logger = logging.getLogger(__name__)


class MqWrapper:
    def __init__(self, url):
        url = furl(url)
        self.host = url.host
        self.port = url.port

        try:
            pika.BlockingConnection(pika.ConnectionParameters(host=self.host, port=self.port))
        except pika.exceptions.AMQPConnectionError:
            raise ConnectionError

    def publish(self, destination, message):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host, port=self.port))
        channel = connection.channel()
        channel.exchange_declare(exchange=destination, exchange_type='fanout')
        channel.basic_publish(exchange=destination, routing_key='', body=message)
        connection.close()

    def consume(self, destination, handler):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host, port=self.port))
        channel = connection.channel()
        channel.exchange_declare(exchange=destination, exchange_type='fanout')
        result = channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue
        channel.queue_bind(exchange=destination, queue=queue_name)

        def callback(channel, method, properties, body):
            handler(body)

        channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
        channel.start_consuming()
