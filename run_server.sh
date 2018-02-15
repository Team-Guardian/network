#!/bin/bash
# Starts server

# Run container in background (detached mode)
sudo docker run --detach \
    -p 1346:80 \
    --mount type=bind,source=$HOME/guardian/www,target=/var/www,readonly \
    --name airserver \
    airserver