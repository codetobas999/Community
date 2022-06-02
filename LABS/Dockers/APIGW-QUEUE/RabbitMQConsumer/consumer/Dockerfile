# basic python image
FROM python:3.7

# install pika to access rabbitmq
RUN pip install pika

# install requests to call REST API
RUN pip install requests

# Without this setting, Python never prints anything out.
ENV PYTHONUNBUFFERED=1

# declare the source directory
WORKDIR /app/consumer

# copy the file
COPY consumer.py .

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "consumer.py" ]

