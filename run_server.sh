#!/bin/bash
# Starts server

# Run container in background (detached mode)
sudo docker run --detach \
    --mount type=bind,source=$HOME/guardian/www,target=/var/www,readonly \
    --name airserver \
    airserver