import http.client
import sys
import logging
from time import sleep
from logging.handlers import RotatingFileHandler

# setup logger and log format
logging.basicConfig(level=logging.DEBUG, format = '[%(levelname)s] %(asctime)s | %(module)s | %(message)s')
logger = logging.getLogger(__name__)

# setup file handler to write logs to a file
debughandler = RotatingFileHandler('client_log.log', maxBytes = 1048576, backupCount = 1)
debughandler.setLevel(logging.DEBUG) #set debug handler level to debug
formatter = logging.Formatter('[%(levelname)s] %(asctime)s | %(module)s | %(message)s')
debughandler.setFormatter(formatter)

#adds file handler to logger
logger.addHandler(debughandler)

while True:
    #server_ip = sys.argv[1]
    try:
        server_ip = "127.0.1.20"
        logger.debug('Target server IP: %s',server_ip)
        x = http.client.HTTPConnection(server_ip, 9999)
        x.connect()
        x.request('GET', '/imgs/imgs-listen.txt')

        y = x.getresponse()
        z = y.read()
        logger.info('GET Response received: %s',z)
        sleep(0.5)
    except ConnectionRefusedError:
        logger.error('Connection refused! Server may be offline. Retrying in 5s...')
        sleep(5)
    except ConnectionResetError:
        logger.error('Connected reset! Server may have stopped. Retrying in 5s...')
        sleep(5)