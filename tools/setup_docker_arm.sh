#!/bin/bash
# Installs Docker

# Update apt package index
sudo apt-get -qq update

# Install packages to allow apt to use the Docker repository over HTTPS
sudo apt-get -qq install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common

# Install Docker Community Edidtion (CE)
sudo apt-get -qq install -y docker.io
