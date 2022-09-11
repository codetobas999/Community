FROM python:3.7-slim
WORKDIR /mnt/code/
COPY requirements.txt /
RUN pip install -U pip \
    && pip install -r /requirements.txt
EXPOSE 8080
