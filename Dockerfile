FROM python

RUN pip install -U bridgecrew
RUN apt-get update
RUN apt install -y git

ENTRYPOINT ["bridgecrew"]
