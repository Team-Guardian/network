import http.server
import os
import sys
import logging #logging library for info, error, etc messages
from logging.handlers import RotatingFileHandler

# load custom deployment settings
from settings import SERVER_BASE_DIR, PORT

# setup logger and log format
logging.basicConfig(level=logging.DEBUG, format = '[%(levelname)s] %(asctime)s | %(module)s | %(message)s')
logger = logging.getLogger(__name__)

# setup file handler to write logs to a file
debughandler = RotatingFileHandler('server_log.log', maxBytes = 1048576, backupCount = 1)
debughandler.setLevel(logging.DEBUG) #set debug handler level to debug
formatter = logging.Formatter('[%(levelname)s] %(asctime)s | %(module)s | %(message)s')
debughandler.setFormatter(formatter)

#adds file handler to logger
logger.addHandler(debughandler)

IMGS_DIR_LISTING_FILEPATH = '/imgs/imgs-listen.txt'
logger.debug('Imgs Directory Filepath: %s', IMGS_DIR_LISTING_FILEPATH)

def updateImagesDirectoryListing(): # Updates the imgs-listen.txt file to represent the current /imgs directory contents
    with open(SERVER_BASE_DIR + IMGS_DIR_LISTING_FILEPATH, 'w') as f:
        dir_listing = os.listdir(SERVER_BASE_DIR + '/imgs') 
                                                # get a list of all imgs in directory
        for item in dir_listing:
            f.write('{}\n'.format(item)) # only keep image filename
    logger.debug('Updated images directory successfully')

class ServerRequestHandler(http.server.BaseHTTPRequestHandler):

    # don't override __init__() method

    def do_GET(self):
        logger.info('Received a GET request')
        self.send_response(200,'OK') # server is OK

        if self.path == IMGS_DIR_LISTING_FILEPATH:
            updateImagesDirectoryListing()

        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        # send requested file
        # with open(SERVER_BASE_DIR + self.path, 'rb') as f:
        #    self.wfile.write(f.read())
        # f.close()

    def do_POST(self):
        logger.info('Received a POST request')

def run(server_ip):
    server_addr = (server_ip, PORT) # define network addr of this machine

    httpd = http.server.HTTPServer(server_addr, ServerRequestHandler) # create the server
    logger.info('Server is running...')
    httpd.serve_forever() # begin listening for events


if __name__ == "__main__":

    # parse arguments for server configuration
    #server_ip = sys.argv[1]

    server_ip = '127.0.1.20'
    logger.info('Starting the server at {}:{}, with filesystem root directory set to {}'.format(server_ip, PORT, SERVER_BASE_DIR))

    run(server_ip) # start up the server