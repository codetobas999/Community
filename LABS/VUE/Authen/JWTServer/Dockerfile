FROM ubuntu
RUN apt-get update
RUN apt-get install -y python-dev-is-python3 python3-pip libffi-dev libssl-dev
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
ADD . .
CMD ["python", "jwt_server.py"]