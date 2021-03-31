"""import pika

from core.models import Ingrediente

params = pika.URLParameters('amqps://cuuvvsiw:U1lZAvckFDDP4R1sfK4fHOEZ0mPYSmhf@hornet.rmq.cloudamqp.com/cuuvvsiw')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(channel, method, properties, body):
    print(f'recebido em admin pela pizzaria')
    Ingrediente.objects.create(nome='ingrediente_teste', descricao='xxx')
    print(body)

channel.basic_consume(queue='admin', on_message_callback=callback)

print(f'started consumind in pizzaria')

channel.start_consuming()

channel.close()"""