import http.server
import os
import sys
from http import HTTPStatus

# load custom deployment settings
from settings import SERVER_BASE_DIR, PORT

class ServerRequestHandler(http.server.BaseHTTPRequestHandler):

    # don't override the __init__() method

    def do_GET(self):
        pass

    def do_POST(self):
        pass

def run(server_ip):
    server_addr = (server_ip, PORT) # define network addr of this machine

    httpd = http.server.HTTPServer(server_addr, ServerRequestHandler) # create the server
    httpd.serve_forever() # begin listening for events

if __name__ == "__main__":

    # parse arguments for server configuration
    server_ip = "localhost"

    #server_ip = '127.0.1.20'
    print('Starting the server at {}:{}, with filesystem root directory set to {}'.format(server_ip, PORT, SERVER_BASE_DIR))

    run(server_ip) # start up the server