#!/bin/bash
PYVERCOMMAND="$( python --version 2>&1)"
PYVERSION=${PYVERCOMMAND:0:8}
if [ "$PYVERSION" = "Python 3" ]
then
    echo "Yup, you old school"
else
    echo "Living on the edge"
fi
