#!/bin/bash
PYVERCOMMAND="$( python --version 2>&1)"
PYVERSION=${PYVERCOMMAND:0:8}
if [ "$PYVERSION" = "Python 3" ]
then
    ./comp_dev_setup_Py3.py
else
    ./comp_dev_setup_Py2.py
fi
