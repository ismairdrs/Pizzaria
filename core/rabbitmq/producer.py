"""
import os

import pika
import sys

from django.conf import settings


class Producer:

    def __init__(self, host, username, password):
        self.connection = pika.BlockingConnection(
            pika.URLParameters(f'amqp://{username}:{password}@{host}:5672')
        )
        self.channel = self.connection.channel()
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


producer = Producer(
    host=os.environ.get('RABBITMQ_HOST'),
    username=os.environ.get('RABBITMQ_USERNAME'),
    password=os.environ.get('RABBITMQ_PASSWORD')
)
"""
import json

"""
import pika
import time
connection = pika.BlockingConnection(
   pika.ConnectionParameters('localhost')
)
channel = connection.channel()

channel.queue_declare(queue='hello')

messages = [
   "Primeira mensagem",
   "Segunda mensagem",
   "Terceira mensagem"
]

for message in messages:
   channel.basic_publish(
      exchange='',
      routing_key='hello',
      body=message
   )
   print(" [x] Enviada '" + message + "'")
   time.sleep(1)

connection.close()
"""

import os
import json
import pika
import sys

from django.conf import settings


class Producer:

    #def __init__(self, host, username, password):
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
            #self.channel.queue_declare(queue='nome_queue')
            self.exchanges.append(exchange)
        self.channel.basic_publish(
            exchange=exchange,
            routing_key=routing_key,
            body=json.dumps(body)
        )
producer = Producer()

"""
producer = Producer(
    host=os.environ.get('RABBITMQ_HOST'),
    username=os.environ.get('RABBITMQ_USERNAME'),
    password=os.environ.get('RABBITMQ_PASSWORD')
)"""