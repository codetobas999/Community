import pika

#connection_parameters = pika.ConnectionParameters('localhost')
connection_parameters = pika.ConnectionParameters('10.138.20.228')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue='letterbox')

message = "Hello this is my first message"

channel.basic_publish(exchange='', routing_key='letterbox', body=message)

print(f"sent message: {message}")

connection.close()