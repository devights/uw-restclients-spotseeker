#!/bin/sh
trap catch ERR

# test script for django app
#
# PRECONDITIONS:
#      * necessary test tooling already installed
#      * inherited env vars MUST include:
#        DJANGO_APP: django application directory name

# start virtualenv
source bin/activate

# install test tooling
pip install coverage

function run_test {
    echo "##########################"
    echo "TEST: $1"
    eval $1
}

function catch {
    echo "Test failure occurred on line $LINENO"
    exit 1
}

run_test "coverage run --source=${DJANGO_APP} --omit=*/migrations/*,${DJANGO_APP}/management/commands/* manage.py test ${DJANGO_APP} --settings=project.settings"

# put generaged coverage result where it will get processed
cp .coverage* /coverage
echo "Looking inside coverage"
ls /coverage

exit 0
