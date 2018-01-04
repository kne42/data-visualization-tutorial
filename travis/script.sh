#!/usr/bin/env bash
set -ex

section_begin conda_info
conda info -a
conda list -e --no-pip
section_end conda_info

section_begin tests
pytest -v
section_end tests
