#from fastapi import FastAPI
#from pydantic import BaseModel
import pika
import os
import time
import requests
import json

# read rabbitmq connection url from environment variable
amqp_url = os.environ['AMQP_URL']
url_params = pika.URLParameters(amqp_url)

# connect to rabbitmq
connection = pika.BlockingConnection(url_params)
chan = connection.channel()

# declare a new queue
# durable flag is set so that messages are retained
# in the rabbitmq volume even between restarts
chan.queue_declare(queue='hello', durable=True)


def receive_msg(ch, method, properties, body):
    print('received msg : ', body.decode('utf-8'))

    request_dict = json.loads(body.decode('utf-8'))
    print(request_dict)

    time.sleep(request_dict['service_sleep'])

     
    print('acking it') 
    #https://www.nylas.com/blog/use-python-requests-module-rest-apis/
    # Create a new resource
    #query = {''}
    #response = requests.get('http://192.168.1.136:3000/mock', params=query)
    #response = requests.get('http://192.168.1.136:3000/mock')
    if request_dict['service_method'] == 'GET' :
        response = requests.get(request_dict['service_url'])
        print(response.json())
        ch.basic_ack(delivery_tag=method.delivery_tag)
    elif request_dict['service_method'] == 'POST' :
        response = requests.post(request_dict['service_url'],data = request_dict['service_input'])
        print(response.json())
        ch.basic_ack(delivery_tag=method.delivery_tag)  
    else :
        print('Error Service Method')     

    

# to make sure the consumer receives only one message at a time
# next message is received only after acking the previous one
chan.basic_qos(prefetch_count=1)

# define the queue consumption
chan.basic_consume(queue='hello', on_message_callback=receive_msg)

print("Waiting to consume")
# start consuming
chan.start_consuming()
 