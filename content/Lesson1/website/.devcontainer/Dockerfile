FROM mcr.microsoft.com/devcontainers/python:3.11

# Install wget and other dependencies if not present
RUN apt-get update && apt-get install -y wget gdebi-core

# Download and install Quarto CLI
RUN wget https://github.com/quarto-dev/quarto-cli/releases/download/v1.3.331/quarto-1.3.331-linux-amd64.deb -O quarto.deb && \
    gdebi -n quarto.deb && \
    rm quarto.deb

# Install Quarto CLI
RUN curl -fsSL https://quarto.org/download/latest/quarto-linux-amd64.deb -o quarto.deb \
    && dpkg -i quarto.deb \
    && rm quarto.deb
