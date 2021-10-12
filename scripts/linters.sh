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
cd "$CWD"
PY_FILES=$(find . -type f -name "*.py" ! -path './.*' -not -path "**/migrations/*" -not -path "**/settings/*")

echo "startesting"

# ===================================================

echo "-----------start mypy-------------------"
mypy $PY_FILES  --exclude migrations


echo "-----------start pycodestyle------------"
pycodestyle $PY_FILES

echo "-----------start flake8-----------------"
flake8 $PY_FILES


echo "-----------start pylint_django-----------------"
pylint --max-line-length=120  --disable=E1101,C0116,C0114,R0903,R0401,R0801,C0413 --load-plugins pylint_django $PY_FILES src
