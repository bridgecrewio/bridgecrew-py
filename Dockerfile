FROM python:3.7-alpine

RUN apk add --no-cache git curl util-linux bash

RUN apk add --no-cache --virtual .build_deps build-base libffi-dev \
 && pip install --no-cache-dir -U bridgecrew \
 && apk del .build_deps

COPY ./github_action_resources/entrypoint.sh /entrypoint.sh
COPY ./github_action_resources/bridgecrew-problem-matcher.json /usr/local/lib/bridgecrew-problem-matcher.json
COPY ./github_action_resources/bridgecrew-problem-matcher-warning.json /usr/local/lib/bridgecrew-problem-matcher-warning.json

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/entrypoint.sh"]
