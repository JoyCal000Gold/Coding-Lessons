FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

# --- 1. System Packages ---
COPY apt.txt /tmp/apt.txt
RUN apt-get update && xargs -a /tmp/apt.txt apt-get install -y && rm -rf /var/lib/apt/lists/*

# --- 2. Install Quarto (Latest) ---
RUN wget https://github.com/quarto-dev/quarto-cli/releases/latest/download/quarto-linux-amd64.deb -O /tmp/quarto.deb && \
    apt install -y /tmp/quarto.deb && \
    rm /tmp/quarto.deb

# --- 3. Install Miniconda ---
ENV CONDA_DIR=/opt/conda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /tmp/miniconda.sh && \
    bash /tmp/miniconda.sh -b -p $CONDA_DIR && \
    rm /tmp/miniconda.sh
ENV PATH="$CONDA_DIR/bin:$PATH"

# --- 4. Set up Conda environment ---
COPY .devcontainer/environment.yml /tmp/environment.yml
RUN conda update -n base -c defaults conda && \
    conda env create -f /tmp/environment.yml && \
    conda clean -afy
SHELL ["conda", "run", "-n", "quarto-env", "/bin/bash", "-c"]

# --- 5. Install Rust ---
RUN curl https://sh.rustup.rs -sSf | bash -s -- -y
ENV PATH="/root/.cargo/bin:$PATH"

# --- 6. Set up R user library & install R packages ---
COPY install.R /tmp/install.R
RUN mkdir -p /root/Rlibs && \
    echo 'R_LIBS_USER="/root/Rlibs"' >> /root/.Renviron && \
    Rscript /tmp/install.R

# --- Final working dir ---
WORKDIR /workspace
