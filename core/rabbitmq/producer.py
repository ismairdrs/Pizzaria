"""import pika
import json

from decouple import config
rabbitmq = config('RABBITMQ')


class Producer():

    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.URLParameters(rabbitmq)
        )
        self.channel = self.connection.channel()
        self.exchanges = []

    def produce(self, exchange, body, routing_key=''):
        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)

        if exchange not in self.exchanges:
            self.channel.exchange_declare(exchange=exchange)
            self.exchanges.append(exchange)


        self.channel.basic_publish(

            exchange=exchange,
            routing_key=routing_key,
            body=json.dumps(body)
        )


producer = Producer()
"""