# basic python image
FROM python:3.7

# install pika to access rabbitmq
RUN pip install pika

# Without this setting, Python never prints anything out.
ENV PYTHONUNBUFFERED=1

# declare the source directory
FROM python:3.7.3-alpine3.8
RUN apk add --no-cache build-base
WORKDIR /app/producer

# copy the file
COPY producer.py .

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD uvicorn producer:app --host 0.0.0.0 --port 80

