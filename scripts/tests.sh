#!/bin/bash

echo ">>> $(basename ${BASH_SOURCE[0]})"

set -o errexit # exit script when command fails
set -o pipefail # this setting prevents errors in a pipeline from being masked
set -o nounset # exit script when it tries to use undeclared variables

# INIT WORKING DIR
# ===================================================
cd "$(dirname "${BASH_SOURCE[0]}")"
FILE_DIR=$(pwd)
cd ..
CWD="$(pwd)"

# RUNNING LINTER
# ===================================================
echo "startesting"

echo "-----------start pytest-------------------"
docker-compose -f docker-compose-test.yml run --rm test_auth bash -c "pytest ."
