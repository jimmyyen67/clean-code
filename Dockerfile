FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    vim \
    git \
    curl \
    && curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g typescript ts-node \
    && rm -rf /var/lib/apt/lists/*

RUN node --version && npm --version && tsc --version

WORKDIR /app