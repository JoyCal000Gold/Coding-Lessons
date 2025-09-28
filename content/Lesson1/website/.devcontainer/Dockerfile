# .devcontainer/Dockerfile
FROM mcr.microsoft.com/devcontainers/python:3.11

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    gdebi-core \
    && rm -rf /var/lib/apt/lists/*

# Install Quarto CLI (pick latest stable version or fix version here)
RUN wget https://github.com/quarto-dev/quarto-cli/releases/download/v1.3.331/quarto-1.3.331-linux-amd64.deb -O quarto.deb && \
    gdebi -n quarto.deb && \
    rm quarto.deb

# Clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/*
