#!/bin/bash
PYVERCOMMAND="$( python --version 2>&1)"
PYVERSION=${PYVERCOMMAND:0:8}
if [ "$PYVERSION" = "Python 3" ]
then
    git branch checkout Python3
    ./CompDevSetup.py
else
    git branch checkout master
    ./CompDevSetup.py
fi
