#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pika
import time
import datetime
import json
import sys
#python worker.py "item 3"

stop_word = sys.argv[1]
max_retries = 3
queue = 'retries'

connection = pika.BlockingConnection(pika.ConnectionParameters('10.138.20.228'))
channel = connection.channel()
channel.queue_declare(queue=queue, durable=True)

print ('[*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
	#print properties.headers.get('hello')
	data = json.loads(body)
	print ("[>] Received '%s' (try: %d)" % (data.get('keyword'), 1 + int(properties.priority)))

	if properties.priority >= max_retries - 1: # example handling retries
		ch.basic_ack(delivery_tag=method.delivery_tag)
		print ("[!] '%s' rejected after %d retries" % (data.get('keyword'), 1 + int(properties.priority)))
	else:
		try:
			if data.get('keyword') == stop_word: # example - rejeceting job
				raise Exception('Stop word detected')

			time.sleep(len(data.get('keyword')))
			ch.basic_ack(delivery_tag=method.delivery_tag)
			print ("[+] Done")

		except:
			timestamp = time.time()
			now = datetime.datetime.now()
			expire = 1000 * int((now.replace(hour=23, minute=59, second=59, microsecond=999999) - now).total_seconds())

			# to reject job we create new one with other priority and expiration
			channel.basic_publish(exchange='', routing_key=queue, body=json.dumps(data),
				properties=pika.BasicProperties(delivery_mode=2, priority=int(properties.priority) + 1, timestamp=timestamp, expiration=str(expire), headers=properties.headers))
			# also do not forget to send back acknowledge about job
			ch.basic_ack(delivery_tag=method.delivery_tag)
			print ("[!] Rejected, going to sleep for a while")
			time.sleep(10)

	print()

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback, queue=queue)

try:
	channel.start_consuming()
except KeyboardInterrupt:
	channel.stop_consuming();

connection.close()