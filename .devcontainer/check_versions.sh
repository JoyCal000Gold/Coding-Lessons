#!/bin/bash

echo "Checking installed versions..."

echo -n "Python version: "
python --version

echo -n "Flask version: "
python -c "import flask; print(flask.__version__)"

echo -n "R version: "
R --version | head -n 1

echo -n "Quarto version: "
quarto --version

echo "Version checks complete."
