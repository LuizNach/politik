# -*- coding: utf-8 -*-
"""
@author: Lwz
"""

import pika

f = open('politicians.json','r')
text = f.read()
'''If we wanted to connect to a broker on a different machine we'd simply specify its name or IP address here.'''
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='politik_politicians')

channel.basic_publish(exchange='', routing_key='politik_politicians', body=text)

print(" [x] Sent {0}".format(text))

connection.close()