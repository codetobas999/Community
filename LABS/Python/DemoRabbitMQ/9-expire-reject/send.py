#!/usr/bin/env python
import pika
import time
import datetime
import json
import sys
#python send.py 6
count = int(sys.argv[1]) # read from command line arguments count of jobs to create
queue = 'retries' # queue name

''' example of more robust pika.ConnectionParameters
host='localhost',
port=5672,
virtual_host='/',
credentials=pika.credentials.PlainCredentials(
	username='guest',
	password='guest'
)
'''
connection = pika.BlockingConnection(pika.ConnectionParameters('10.138.20.228'))
channel = connection.channel()
channel.queue_declare(queue=queue, durable=True) # durable=True - makes queue persistent

for i in range(1, count + 1):
	message = "item %d" % i
	timestamp = time.time()
	now = datetime.datetime.now()
	#expire = 1000 * int((now.replace(hour=23, minute=59, second=59, microsecond=999999) - now).total_seconds())
	expire = 10000
	print ("[>] expire %d" % expire)
	headers = { # example how headers can be used
		'hello': 'world',
		'created': int(timestamp)
	}
	data = { # example hot to transfer objects rather than string using json.dumps and json.loads
		'keyword': message,
		'domain': message,
		'created': int(timestamp),
		'expire': expire
	}
	channel.basic_publish(
		exchange='',
		routing_key=queue,
		body=json.dumps(data), # must be string
		properties=pika.BasicProperties(
			delivery_mode=2, # makes persistent job
			priority=0, # default priority
			timestamp=timestamp, # timestamp of job creation
			expiration=str(expire), # job expiration (milliseconds from now), must be string, handled by rabbitmq
			headers=headers
		))
	print ("[>] Sent %r" % message)

connection.close()
