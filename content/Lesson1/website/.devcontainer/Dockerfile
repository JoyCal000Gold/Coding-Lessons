FROM mcr.microsoft.com/devcontainers/python:3.11

# Install wget, curl, gdebi-core, and dependencies for Quarto
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    gdebi-core \
    && rm -rf /var/lib/apt/lists/*

# Download and install Quarto CLI (choose either wget or curl, here using wget + gdebi)
RUN wget https://github.com/quarto-dev/quarto-cli/releases/download/v1.3.331/quarto-1.3.331-linux-amd64.deb -O quarto.deb && \
    gdebi -n quarto.deb && \
    rm quarto.deb

# (Optional) Clean up APT cache to reduce image size
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

