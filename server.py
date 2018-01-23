import http.server
import os
import sys

# load custom deployment settings
from settings import SERVER_BASE_DIR, PORT

IMGS_DIR_LISTING_FILEPATH = '/imgs/imgs-listing.txt'

def updateImagesDirectoryListing():
    with open(SERVER_BASE_DIR + IMGS_DIR_LISTING_FILEPATH, 'w') as f:
        dir_listing = os.listdir(SERVER_BASE_DIR + '/imgs') 
                                                # get a list of all imgs in directory
        for item in dir_listing:
            f.write('{}\n'.format(item)) # only keep image filename

class ServerRequestHandler(http.server.BaseHTTPRequestHandler):

    # don't override __init__() method

    def do_GET(self):
        print('Received a GET request')
        self.send_response(200) # server is OK

        # if self.path == IMGS_DIR_LISTING_FILEPATH:
        #     updateImagesDirectoryListing()

        # self.send_header('Content-type', 'text/plain')
        # self.end_headers()

        # # send requested file
        # with open(SERVER_BASE_DIR + self.path, 'rb') as f:
        #     self.wfile.write(f.read())
        # f.close()

    def do_POST(self):
        print('Received a POST request')

def run(server_ip):
    server_addr = (server_ip, PORT) # define network addr of this machine

    httpd = http.server.HTTPServer(server_addr, ServerRequestHandler) # create the server
    print('Server is running...')
    httpd.serve_forever() # begin listening for events

if __name__ == "__main__":

    # parse arguments for server configuration
    server_ip = sys.argv[1]

    print('Starting the server at {}:{}, with filesystem root directory set to {}'.format(server_ip, PORT, SERVER_BASE_DIR))

    run(server_ip) # start up the server