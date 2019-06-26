#!/bin/bash -e

DOCKER_REPO="${DOCKER_REPO:-bloodorangeio/pykubachu}"
DOCKER_TAG="${DOCKER_TAG:-latest}"

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd $DIR

docker build . -t ${DOCKER_REPO}:${DOCKER_TAG}
docker push ${DOCKER_REPO}:${DOCKER_TAG}
