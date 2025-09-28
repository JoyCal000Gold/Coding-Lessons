FROM mcr.microsoft.com/devcontainers/python:3.11

# Install Quarto CLI
RUN curl -fsSL https://quarto.org/download/latest/quarto-linux-amd64.deb -o quarto.deb \
    && dpkg -i quarto.deb \
    && rm quarto.deb
