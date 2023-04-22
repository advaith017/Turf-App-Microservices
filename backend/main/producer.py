#amqps://snxepbsn:0bzaE30YLkSpSbY0uUUHdupEZzebQ0Gk@sparrow.rmq.cloudamqp.com/snxepbsn


import pika,json

params = pika.URLParameters('amqps://snxepbsn:0bzaE30YLkSpSbY0uUUHdupEZzebQ0Gk@sparrow.rmq.cloudamqp.com/snxepbsn')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='',routing_key='admin',body=json.dumps(body), properties=properties)
