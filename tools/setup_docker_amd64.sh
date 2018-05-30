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

# Add Docker's official GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

# Set up stable Docker repository
sudo add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) \
    stable"

# Update apt package index with added repositories
sudo apt-get -qq update

# Install Docker Community Edidtion (CE)
sudo apt-get -qq install -y docker-ce