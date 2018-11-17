import http.server
import os
import sys
from http import HTTPStatus

# load custom deployment settings
from settings import SERVER_BASE_DIR, PORT    #Linux

# SERVER_BASE_DIR = os.getcwd()                   #Windows
# PORT = 5000

content_type_dict = {'.jpg':'image/jpeg', 
                    '.jpeg':'image/jpeg', 
                    '.txt':'text/plain'}

class ServerRequestHandler(http.server.BaseHTTPRequestHandler):

    # don't override the __init__() method

    def sendDirectoryList(self):
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        
        for listing in os.listdir(self.path): 
            self.wfile.write(listing.encode())
            self.wfile.write('\n'.encode()) 
                            # convert str to byte stream and send with separators

    def sendHeaders(self):
        _, file_ext = os.path.splitext(self.path) # get file extension
        try:
            self.send_header('Content-type', content_type_dict[file_ext])
        except:
            pass # add logging and error handling here
        self.end_headers()

    def sendFile(self):
        with open(self.path, 'rb') as f:
            self.wfile.write(f.read())
        f.close()

    def do_HEAD(self): # request not supported
        self.send_error(HTTPStatus.METHOD_NOT_ALLOWED)

    def do_GET(self):
        self.path = SERVER_BASE_DIR + self.path.replace('%20',' ') # modify the path to serve from root directory
        print(self.path)
        print("\n\n")
        if not os.path.exists(self.path): # requested file/directory doesn't exist
            self.send_error(HTTPStatus.NOT_FOUND)
            return

        self.send_response(HTTPStatus.OK) # by now we know we're OK

        if os.path.isdir(self.path): # general request for directory listing
            self.sendDirectoryList()
            return

        # if path is not a directory, it's a file
        self.sendHeaders()
        self.sendFile()
        
    def do_POST(self): #Use the post request to upload files.
        print('Obtained file with content length of {}'.format(self.headers['Content-Length']))
        item = self.rfile.read(int(self.headers['Content-Length']))

        #Write file
        with open(SERVER_BASE_DIR + self.path,'wb') as f:
            f.write(item)

        self.send_response(HTTPStatus.OK) #Send the ok signal
        self.end_headers()

def run(server_ip):
    httpd = http.server.HTTPServer((server_ip, PORT), ServerRequestHandler) # create the server
    print('Server running at {}:{}, with filesystem root directory set to {}'.format(server_ip, PORT, SERVER_BASE_DIR))
    httpd.serve_forever() # begin listening for events

if __name__ == "__main__":
    server_ip = "0.0.0.0"
    run(server_ip) # start up the server