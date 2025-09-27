#!/usr/bin/env bash
set -eux

# Reload conda
source /opt/conda/etc/profile.d/conda.sh
conda activate quarto-env

# Make sure python path is known to R
PYTHON_PATH=$(which python)
echo '
library(reticulate)
use_python("'"$PYTHON_PATH"'", required = TRUE)
' > /tmp/set_python.R
Rscript /tmp/set_python.R

# Reinstall R packages (optional safety net)
Rscript install.R

