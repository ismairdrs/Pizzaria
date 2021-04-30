import json
from random import randint
from time import sleep

from channels.generic.websocket import WebsocketConsumer


class WSConsumer(WebsocketConsumer):
    STATUS = [
        'Preparando envio do pedido',
        'Pedido recebido pelo restaurante',
        'Sua pizza está sendo preparada...',
        'Pizza pronta! Saindo para a entrega...',
        'Seu pedido está chegando...',
        'Pedido Entregue!'
    ]

    def connect(self):
        self.accept()
        for status in self.STATUS:
            self.send(json.dumps({'message': status}))
            sleep(3)
