FROM python

RUN pip install -U bridgecrew

ENTRYPOINT ["bridgecrew"]
