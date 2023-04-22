
import pika
import json
import django
from sys import path
from os import environ

path.append('/home/advaith/HPE/backend/admin/admin/settings.py')
environ.setdefault('DJANGO_SETTINGS_MODULE','admin.settings')
django.setup()
from turfs.models import Turfs

params = pika.URLParameters('amqps://snxepbsn:0bzaE30YLkSpSbY0uUUHdupEZzebQ0Gk@sparrow.rmq.cloudamqp.com/snxepbsn')

connection = pika.BlockingConnection(params)

channel = connection.channel()


channel.queue_declare(queue='admin')

def callback(ch,method,properties,body):
    print("Recieved in admin")
    data=json.loads(body)
    print(data)
    turf = Turfs.objects.get(id=data)
    turf.booked = 1
    turf.save()
    print("Turf booked successfully!")


    

channel.basic_consume(queue='admin',on_message_callback=callback,auto_ack= True)


print('Started consuming')

channel.start_consuming()

channel.close()