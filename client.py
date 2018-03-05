import http.client
import sys
import os
import time
from http import HTTPStatus
from settings import PORT, CLIENT_BASE_DIR, SERVER_IMG_DIR, CLIENT_IMG_DIR

class Client():
    def __init__(self, server_ip):
        self.server_ip = server_ip

        self.server_images = []
        self.local_images = []

        self.server_connection = http.client.HTTPConnection(self.server_ip, PORT)

    def buildLocalImageDirectoryList(self): # build a list of locally hosted images
        for file in os.listdir('{}/{}'.format(CLIENT_BASE_DIR, CLIENT_IMG_DIR)): 
            if file.endswith('.jpg'):
                self.local_images.append(file)

    # Get server directory list
    def requestImageDirectoryList(self):
        try:
            self.server_connection.request('GET', '{}/'.format(SERVER_IMG_DIR))
        except:
            return # try again later
        
        try:
            self.server_images = self.server_connection.getresponse()
        except http.client.RemoteDisconnected:
            self.server_connection.close() # close connection now and try again later
            return
        
        self.server_images = self.server_images.read().decode('utf-8').splitlines()

    def requestNewImages(self):
        for image in self.server_images:
            if image not in self.local_images:
                try:
                    self.server_connection.request('GET', '{}/{}'.format(SERVER_IMG_DIR, image))
                except:
                    return

                if self.saveImage(image) is True:
                    self.local_images.append(image) # add image to the list if it was successfully saved

    def saveImage(self, image_name):
        with open('{}/{}/{}'.format(CLIENT_BASE_DIR, CLIENT_IMG_DIR, image_name), 'wb') as f:
            try:
                image = self.server_connection.getresponse()
            except http.client.RemoteDisconnected:
                self.server_connection.close() # connection will be re-opened on next request
                return False
            f.write(image.read())
        f.close()
        return True

if __name__ == "__main__":
    client = Client(sys.argv[1])
    client.buildLocalImageDirectoryList()

    while True:
        client.requestImageDirectoryList()
        client.requestNewImages()
        time.sleep(0.2)
