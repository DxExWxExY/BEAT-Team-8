#!/usr/bin/env bash

if command -v python3 &>/dev/null; then
    pip3 install pyqt5
    pip3 install pymongo
    pip3 install r2pipe
    pip3 install python-Levenshtein
    pip3 install fuzzywuzzy
    pip3 install xmlschema
else
    echo "Please install python 3 before running the installation script"
fi