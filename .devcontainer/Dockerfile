FROM ubuntu:24.04

ARG DEBIAN_FRONTEND=noninteractive

# --- System-level dependencies (your apt.txt contents)
COPY apt.txt /tmp/apt.txt
RUN apt-get update && xargs -a /tmp/apt.txt apt-get install -y && rm -rf /var/lib/apt/lists/*

# --- Install Rust
RUN curl https://sh.rustup.rs -sSf | bash -s -- -y
ENV PATH="/root/.cargo/bin:$PATH"

# --- Install Miniconda
ENV CONDA_DIR=/opt/conda
RUN curl -fsSL https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o /tmp/miniconda.sh && \
    bash /tmp/miniconda.sh -b -p $CONDA_DIR && \
    rm /tmp/miniconda.sh
ENV PATH="$CONDA_DIR/bin:$PATH"

# --- Install Conda env (if environment.yml exists)
COPY .devcontainer/environment.yml /tmp/environment.yml
RUN conda update -n base -c defaults conda && \
    conda env create -f /tmp/environment.yml && \
    conda clean -afy

# --- Activate env + install pip packages (if needed)
COPY .devcontainer/requirements.txt /tmp/requirements.txt
RUN conda run -n quarto-env pip install -r /tmp/requirements.txt

# --- Install R packages
COPY install.R /tmp/install.R
RUN Rscript /tmp/install.R

# --- Install Quarto CLI (latest)
RUN wget https://github.com/quarto-dev/quarto-cli/releases/latest/download/quarto-linux-amd64.deb -O /tmp/quarto.deb && \
    apt install -y /tmp/quarto.deb && rm /tmp/quarto.deb

# --- Default shell
SHELL ["conda", "run", "-n", "quarto-env", "/bin/bash", "-c"]

WORKDIR /workspaces/${REPO_NAME}

