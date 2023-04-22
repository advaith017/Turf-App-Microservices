
import pika,json

from main import Turf, db

params = pika.URLParameters('amqps://snxepbsn:0bzaE30YLkSpSbY0uUUHdupEZzebQ0Gk@sparrow.rmq.cloudamqp.com/snxepbsn')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')

def callback(ch,method,properties,body):
    print("Recieved in main")
    data = json.loads(body)
    print(data)

    if properties.content_type =='turf_created':
        turf = Turf(id=data['id'],title=data['title'],date=data['date'],time=data['time'])
        db.session.add(turf)
        db.session.commit()
        print('Turf created')

    elif properties.content_type =='turf_updated':
        turf = Turf.query.get(data['id'])
        turf.title = data['title']
        turf.date = data['date']
        turf.time = data['time']
        db.session.commit()
        print('Turf updated')

    elif properties.content_type == 'turf_deleted':
        turf = Turf.query.get(data)
        db.session.delete(turf)
        db.session.commit()
        print('Turf deleted')

channel.basic_consume(queue='main',on_message_callback=callback, auto_ack= True)


print('Started consuming')

channel.start_consuming()

channel.close()