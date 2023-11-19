#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

if [[ ! -x ".venv/bin/python" ]]; then
    echo "Please create a virtual environment and install dependencies (see README.md)"

    exit 1
fi

source .venv/bin/activate

python huawei2mqtt.py
