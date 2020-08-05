FROM python:3.8-slim-buster

RUN pip install -U bridgecrew
RUN apt-get update
RUN apt install -y git curl

ENTRYPOINT ["bridgecrew"]
