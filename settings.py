import os

class Settings:
   def __init__(self,
   	IP_ADDRESS='127.0.0.1',
    PORT=5001,
    SERVER_BASE_DIR=os.getcwd(),
    SERVER_IMG_DIR="/img",
    CLIENT_BASE_DIR=os.getcwd()+"/client_DIR",
    CLIENT_IMG_DIR="/client_img",
    CONFIG_FILENAME="/config.txt"
   	):

       self.CLIENT_BASE_DIR = CLIENT_BASE_DIR
       self.CLIENT_IMG_DIR = CLIENT_IMG_DIR
       self.CONFIG_FILENAME = CONFIG_FILENAME
       self.CONFIG = self.CLIENT_BASE_DIR + self.CONFIG_FILENAME
       self.SERVER_BASE_DIR = SERVER_BASE_DIR
       self.SERVER_IMG_DIR = SERVER_IMG_DIR
       self.PORT = PORT
       self.IP_ADDRESS = IP_ADDRESS

#
# Client-specific settings
#

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
PORT = 5001
