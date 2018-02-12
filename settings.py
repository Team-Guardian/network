import os

#
# Client-specific settings
#

#
# Server-specific settings
#

# All requests to the server are relative to SERVER_BASE_DIR
SERVER_BASE_DIR = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))

#
# Common settings
#

# Port the server will accept requests on
PORT = 9999