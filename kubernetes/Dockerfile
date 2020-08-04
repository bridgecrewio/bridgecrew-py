FROM  python:3.8-slim-buster

COPY kubernetes/requirements.txt /requirements.txt

RUN pip install -r /requirements.txt
RUN apt-get update
RUN apt install -y git curl

RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl \
    && chmod +x kubectl && mv kubectl /usr/local/bin
RUN groupadd -g 12000 -r bridgecrew && useradd -u 12000 --no-log-init -r -g bridgecrew bridgecrew
RUN mkdir /data && mkdir /app && mkdir /home/bridgecrew
RUN chown bridgecrew:bridgecrew /data /app /home/bridgecrew

COPY kubernetes/run_bridgecrew.sh /app
RUN chown bridgecrew:bridgecrew /app/run_bridgecrew.sh && chmod +x /app/run_bridgecrew.sh

ENTRYPOINT ["/app/run_bridgecrew.sh"]
