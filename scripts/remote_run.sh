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

ssh root@64.227.117.166 cd /home/andrew | docker-compose build
ssh root@64.227.117.166 cd /home/andrew | docker-compose up
