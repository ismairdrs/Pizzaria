import pika


class Consumer:

    def __init__(self):
        self.channel = None
        self.connection = None

    def _init_channel(self):
        self.connection = pika.BlockingConnection(
            pika.URLParameters('amqps://cuuvvsiw:U1lZAvckFDDP4R1sfK4fHOEZ0mPYSmhf@hornet.rmq.cloudamqp.com/cuuvvsiw')
        )
        self.channel = self.connection.channel()
        return self.channel

    def _init_queue(self, exchange, queue_name, routing_key):
        queue = self.channel.queue_delcare(queue=queue_name)
        self.channel.queue_bind(
            exchange=exchange,
            queue=queue_name,
            routing_key=routing_key
        )
        return queue

    def consume(self, exchange, queue_name, routing_key, callback):
        channel = self._init_channel()
        queue_name = self._init_queue()
        channel.basic_consume(
            queue=queue_name,
            on_message_callback=callback
        )


consumer = Consumer()
