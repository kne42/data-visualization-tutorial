#!/usr/bin/env bash
set -ex

download () { curl $1 > install.sh; }

section_begin () { echo -en "travis_fold:start:$1\r"; }

section_end () { echo -en "travis_fold:end$1\r"; }

export -f download
export -f section_begin
export -f section_end

set +ex
