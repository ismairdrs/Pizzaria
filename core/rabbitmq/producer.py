import pika
import json

from decouple import config
rabbitmq = config('RABBITMQ')


class Producer():
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.URLParameters(rabbitmq)
        )
        self.channel = self.connection.channel()
        self.exchanges = []

    def produce(self, exchange, body, routing_key=''):
        if exchange not in self.exchanges:
            self.channel.exchange_declare(exchange=exchange)
            self.exchanges.append(exchange)

        self.channel.basic_publish(
            exchange=exchange,
            routing_key=routing_key,
            body=json.dumps(body),
            properties=pika.BasicProperties(
                delivery_mode=2,  # make message persistent
            )
        )

    def close_connection(self):
        self.channel.close()

#producer = Producer()
