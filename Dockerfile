FROM python:3.7-alpine

RUN apk update && apk add --no-cache git curl util-linux bash

RUN pip install --no-cache-dir -U bridgecrew

COPY ./github_action_resources/entrypoint.sh /entrypoint.sh
COPY ./github_action_resources/bridgecrew-problem-matcher.json /usr/local/lib/bridgecrew-problem-matcher.json
COPY ./github_action_resources/bridgecrew-problem-matcher-softfail.json /usr/local/lib/bridgecrew-problem-matcher-softfail.json

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/entrypoint.sh"]
