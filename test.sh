#!/bin/sh

for dir in */test_*.py; do
    cd $(dirname $dir) && pipenv run pytest && cd ..
done
