#!/usr/bin/env bash

set -ex

conda list -e --no-pip

jupyter notebook -y --no-browser &

LIST=`jupyter notebook list`; echo "$LIST"

if [[ "$LIST" == "Currently running servers:" ]]; then
    exit 1
fi
