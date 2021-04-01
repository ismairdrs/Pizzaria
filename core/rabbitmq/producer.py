import json
import pika
"""
    esse é um producer manual
"""

class Producer:

    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters('localhost')
        )
        self.channel = self.connection.channel()
        # as exchanges separam dominios
        # por exemplo likes, users, pizzas,
        self.exchanges = []

    def produce(self, exchange, body, routing_key=''):
        if exchange not in self.exchanges:
            self.channel.declare_exchange(exchange=exchange)
            self.exchanges.append(exchange)
        self.channel.basic_publish(
            exchange=exchange,
            routing_key=routing_key,
            body=json.dumps(body)
        )
producer = Producer()
