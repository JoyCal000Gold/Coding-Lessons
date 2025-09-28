#!/bin/bash

echo "Checking installed versions..."

# Ensure conda is available
if ! command -v conda &> /dev/null; then
  echo "Conda not found"
  exit 1
fi

# Activate environment if not active
if [[ "$CONDA_DEFAULT_ENV" != "quarto-env" ]]; then
  source ~/miniconda3/etc/profile.d/conda.sh 2>/dev/null || source /opt/conda/etc/profile.d/conda.sh
  conda activate quarto-env
fi


echo -n "Python version: "
python --version

echo -n "Flask version: "
python -c "import flask; print(flask.__version__)"

echo -n "R version: "
R --version | head -n 1

echo -n "Quarto version: "
quarto --version

echo "Version checks complete."
