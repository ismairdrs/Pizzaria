import pika

params = pika.URLParameters('amqps://cuuvvsiw:U1lZAvckFDDP4R1sfK4fHOEZ0mPYSmhf@hornet.rmq.cloudamqp.com/cuuvvsiw')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    channel.basic_publish(
        exchange='',
        routing_key='admin',
        body=body
    )

