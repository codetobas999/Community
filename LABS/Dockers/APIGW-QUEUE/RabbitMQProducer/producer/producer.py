from fastapi import FastAPI
from pydantic import BaseModel
import pika
import os
import json

# read rabbitmq connection url from environment variable
amqp_url = os.environ['AMQP_URL']
url_params = pika.URLParameters(amqp_url)

'''
# connect to rabbitmq
connection = pika.BlockingConnection(url_params)
channel = connection.channel()

# declare a new queue
# durable flag is set so that messages are retained
# in the rabbitmq volume even between restarts
channel.queue_declare(queue='hello', durable=True)

'''
app = FastAPI() 

class RequestInfo(BaseModel):
    param_queue_name:str
    param_exchange_name:str
    param_routing_key_name:str

    service_method:str
    service_url:str
    #service_type:str
    service_sleep:int
    service_input:str

@app.post("/registerqueue")
def api(request_item: RequestInfo):
    print("IN Loop register")  

    # connect to rabbitmq
    print(url_params) 
    connection = pika.BlockingConnection(url_params)

    channel = connection.channel()

    param_queue_name=request_item.param_queue_name              #'queue'
    param_exchange_name=request_item.param_exchange_name        #''
    param_routing_key_name=request_item.param_routing_key_name  #'hello'
    #param_body_str=request_item.param_body_str                  #'hello world'

    param_body_dict = {
        #"params_info": {
            "param_queue_name":param_queue_name ,
            "param_exchange_name":param_exchange_name,
            "param_routing_key_name":param_routing_key_name ,
        #},
        #"service_info": {
            "service_method":request_item.service_method ,
            "service_url":request_item.service_url,            
            "service_sleep":request_item.service_sleep,
            "service_input":request_item.service_input  
        #} 
    }
    param_body_str = json.dumps(param_body_dict)
    print(param_body_str)  
    # declare a new queue
    # durable flag is set so that messages are retained
    # in the rabbitmq volume even between restarts
    channel.queue_declare(queue=param_queue_name, durable=True)
    
    channel.basic_publish(exchange=param_exchange_name, routing_key=param_routing_key_name,body=param_body_str, properties=pika.BasicProperties(delivery_mode=2))
    print("Produced the message")
    # close the channel and connection
    # to avoid program from entering with any lingering
    # message in the queue cache
    #chan.close()
    #connection.close()
    return {'results': 'registered'}