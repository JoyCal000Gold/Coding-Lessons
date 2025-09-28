FROM mcr.microsoft.com/devcontainers/python:3.11

# Install dependencies
RUN apt-get update && apt-get install -y \
  wget \
  curl \
  gdebi-core \
  && rm -rf /var/lib/apt/lists/*

# Download and install Quarto CLI (version v1.6.43)
RUN wget https://github.com/quarto-dev/quarto-cli/releases/download/v1.6.43/quarto-1.6.43-linux-amd64.deb -O quarto.deb && \
  gdebi -n quarto.deb && \
  rm quarto.deb

# Clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Ensure quarto is in PATH
ENV PATH="/usr/local/bin:${PATH}"
