FROM python:3.8-slim

RUN apt-get update -y && apt-get install curl git -y && pip install --no-cache-dir -U bridgecrew

COPY ./github_action_resources/entrypoint.sh /entrypoint.sh
COPY ./github_action_resources/bridgecrew-problem-matcher.json /usr/local/lib/bridgecrew-problem-matcher.json
COPY ./github_action_resources/bridgecrew-problem-matcher-warning.json /usr/local/lib/bridgecrew-problem-matcher-warning.json

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/entrypoint.sh"]
