class Settings:
   def __init__(self, IP_ADDRESS, PORT, SERVER_BASE_DIR):
       self.CLIENT_BASE_DIR = "/var/www/client_dir/"
       self.CLIENT_IMG_DIR ="/client_img"
       self.CONFIG_FILENAME = '/config.txt'
       self.CONFIG = self.CLIENT_BASE_DIR + self.CONFIG_FILENAME
       self.SERVER_BASE_DIR = SERVER_BASE_DIR
       self.SERVER_IMG_DIR = "/img"
       self.PORT = PORT
       self.IP_ADDRESS = IP_ADDRESS

#
# Client-specific settings
#

import os

CLIENT_BASE_DIR = os.getcwd() + "/client_DIR"
CLIENT_IMG_DIR = "/client_img"

CONFIG_FILENAME = '/config.txt'
CONFIG = CLIENT_BASE_DIR + CONFIG_FILENAME


#
# Server-specific settings
#

# All requests to the server are relative to SERVER_BASE_DIR
SERVER_BASE_DIR = os.getcwd()
SERVER_IMG_DIR = "/img"


#
# Common settings
#

# Port the server will accept requests on
PORT = 1347
