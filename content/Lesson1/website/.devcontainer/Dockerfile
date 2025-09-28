# .devcontainer/Dockerfile
FROM mcr.microsoft.com/devcontainers/python:3.11

# Install dependencies and Quarto CLI in one RUN command
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    gdebi-core && \
    wget https://github.com/quarto-dev/quarto-cli/releases/download/v1.3.331/quarto-1.3.331-linux-amd64.deb -O quarto.deb && \
    gdebi -n quarto.deb && \
    rm quarto.deb && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Ensure /usr/local/bin is in PATH (where quarto is usually installed)
ENV PATH="/usr/local/bin:${PATH}"
