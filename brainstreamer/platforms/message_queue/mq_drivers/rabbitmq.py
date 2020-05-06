import pika


class RabbitMq:
    scheme = 'rabbitmq'

    def __init__(self, host, port):
        self.host = host
        self.port = port

        try:
            pika.BlockingConnection(pika.ConnectionParameters(host=self.host, port=self.port))
        except pika.exceptions.AMQPConnectionError:
            raise ConnectionError

    def publish(self, topic, message):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host, port=self.port))
        channel = connection.channel()
        channel.exchange_declare(exchange=topic, exchange_type='fanout')
        channel.basic_publish(exchange=topic, routing_key='', body=message)
        connection.close()

    def consume(self, topic, handler):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host, port=self.port))
        channel = connection.channel()
        channel.exchange_declare(exchange=topic, exchange_type='fanout')
        result = channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue
        channel.queue_bind(exchange=topic, queue=queue_name)

        def callback(channel, method, properties, body):
            handler(body)

        channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
        channel.start_consuming()
