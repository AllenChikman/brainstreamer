import pika


class RabbitMQ:  # TODO: remove prints
    prefix = 'rabbitmq'

    def __init__(self, host, port):
        self.host = host
        self.port = port

        try:  # test connection
            pika.BlockingConnection(pika.ConnectionParameters(host=self.host, port=self.port))
        except pika.exceptions.AMQPConnectionError:
            raise ConnectionError

    def publish(self, topic, message):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host, port=self.port))
        channel = connection.channel()
        channel.exchange_declare(exchange=topic, exchange_type='fanout')
        channel.basic_publish(exchange=topic, routing_key='', body=message)
        connection.close()
        # print('Message sent to queue')

    def consume(self, topic, handler):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host, port=self.port))
        channel = connection.channel()
        channel.exchange_declare(exchange=topic, exchange_type='fanout')
        result = channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue
        channel.queue_bind(exchange=topic, queue=queue_name)

        def callback(channel, method, properties, body):
            handler(body)
            # print("Handled message from queue")

        channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
        # print('Waiting for messages')
        channel.start_consuming()
