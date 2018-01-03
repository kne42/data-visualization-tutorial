#!/usr/bin/env bash
set -ex

conda info -a

section_begin tests
pytest
section_end tests
