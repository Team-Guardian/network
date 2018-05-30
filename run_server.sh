#!/bin/bash
# Starts server

# Run container in background (detached mode)
sudo docker run --detach \
    -p 1346:1346 \
    --volume /var/www:/var/www:ro \
    --name airserver \
    airserver
