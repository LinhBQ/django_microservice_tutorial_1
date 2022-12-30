import pika

params = pika.URLParameters('amqps://qoutfarr:s2fNjLfPX53r2-qqhRSBcudmvWtXvN9h@armadillo.rmq.cloudamqp.com/qoutfarr')

conection = pika.BlockingConnection(params)

channel = conection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='main', body='hello main')