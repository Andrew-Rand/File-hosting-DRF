#!/bin/bash

echo ">>> $(basename ${BASH_SOURCE[0]})"

set -o errexit # exit script when command fails
set -o pipefail # this setting prevents errors in a pipeline from being masked
set -o nounset # exit script when it tries to use undeclared variables

# INIT WORKING DIR
# ===================================================
cd "$(dirname "${BASH_SOURCE[0]}")"
cd ..
CWD="$(pwd)"

# Lint project before deploy
./scripts/linters.sh
./scripts/tests.sh

#  Kill remote project
ssh root@64.227.117.166 "cd /home/andrew && docker-compose down"
ssh root@64.227.117.166 "cd /home/andrew && sudo rm -r src/ srv/ static/ .env docker-compose.yml entrypoint.sh manage.py Pipfile Pipfile.lock"

# Deploy new version
tar -zcf archive_to_deploy.tar.gz src/ srv/ static/ .env docker-compose.yml entrypoint.sh manage.py Pipfile Pipfile.lock
scp archive_to_deploy.tar.gz root@64.227.117.166:/home/andrew
ssh root@64.227.117.166 "cd /home/andrew && tar -xzf archive_to_deploy.tar.gz"

# Run new version
ssh root@64.227.117.166 "cd /home/andrew && docker-compose build"
ssh root@64.227.117.166 "cd /home/andrew && docker-compose up"
