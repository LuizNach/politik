import pika
import json
import string
import random
from politik.models import Politician
from django.contrib.auth.models import User

def read_queues():
    credentials = pika.PlainCredentials('guest', 'guest')
    parameters = pika.ConnectionParameters('ec2-54-149-173-164.us-west-2.compute.amazonaws.com',
                                           5672,
                                           '/',
                                           credentials)

    connection = pika.BlockingConnection(parameters)

    channel = connection.channel()

    channel.queue_declare(queue='politik_politicians')

    channel.basic_consume(callback, queue='politik_politicians', no_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


def start_manager():
    import threading
    t = threading.Thread(target=read_queues, args=(), kwargs={})
    t.setDaemon(True)
    t.start()
    return



def callback(ch, method, properties, body):
    data = json.loads(body)
    print(data)
    for pol in data["dados"]:
        # polUser = User()
        username = str(pol["nome"])
        politician = Politician()
        user = User.objects.create_user(username=username.strip(" "),
                                 email=''.join(random.choices(string.ascii_uppercase + string.digits, k=10)),
                                 password=''.join(random.choices(string.ascii_uppercase + string.digits, k=10)))

        politician.foreign_id = pol["id"]
        politician.location = pol["siglaUf"]
        politician.name = pol["nome"]
        politician.party = pol["siglaPartido"]
        politician.photoURL = pol["urlFoto"]
        politician.user = user
        politician.save()
        print(politician)
        print(user)
