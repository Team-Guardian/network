import http.client
import os, time
import logging
from settings import PORT, CLIENT_DIR, CONFIG_FILENAME, CONFIG         #Linux

# CLIENT_DIR = os.getcwd() + '\\client_imgs\\'    #Windows
# CONFIG = os.getcwd() + '\\client_imgs\\demo.txt' #CONFIG file location
# CONFIG_FILENAME = '/demo.txt'
# PORT=5000

logging.basicConfig(filename="logfile.log", filemode="w", level=logging.DEBUG,
format="%(asctime)s %(levelname)s: %(message)s", datefmt="%d/%b/%Y %H:%M:%S")


class Client(object):
        def __init__(self, server_ip = "localhost"):
            self.client_list = []
            self.server_list = []
            self.server_ip = server_ip #sys.argv[1]
            self.server_connection = http.client.HTTPConnection(self.server_ip, PORT)
            for file in os.listdir(CLIENT_DIR):
                if file.endswith('.jpg'):
                    self.client_list.append(file)

        # Description:
        #     Uploads the config file into the server.
        #     Global variables used: (CONFIG and CONFIG_FILENAME)
        # Return:
        #     True            - Success
        #     False           - Fails
        #Uploads the config file
        #Chosen by the CONFIG and CONFIG_FILENAME global variables
        def uploadConfig(self):
            try:
                with open(CONFIG, 'rb') as f:
                    item = f.read()
                self.server_connection.request('POST', CONFIG_FILENAME,item)
                print(self.server_connection.getresponse().status)
                self.server_connection.close()
                return True
            except Exception as err:
                self.clientExceptionHandler(err)
                return False

        # Description:
        #     Obtains the server directory list. Places it into self.server_list
        # Return:
        #     True            - Success
        #     False           - Fails
        def requestServer(self):
            try:
                self.server_connection.request('GET', '/img/')
                self.server_list = self.server_connection.getresponse().read().decode("utf-8").splitlines()
                self.server_connection.close()
                return True
            except Exception as err:
                self.clientExceptionHandler(err)
                return False
                
        # Description:
        #    Downloads the latest files. Retries until it recieves the files.
        # Parameters:
        #     retryLimit         - Number of tries it should do (Must be positive)
        # Return:
        #     True               - Success
        #     False              - Fails
        def updateClientFiles(retryLimit=None):
            count = 1
            while(not(self.updateClientList()) and (retryLimit == None or count < retryLimit)):
                count += 1
            return True if (count > retryLimit) else False

        # Description:
        #     Downloads all files that are not in self.client_list
        # Return:
        #     True                - Success
        #     False               - Fails
        def updateClientList(self):
            try:
                #Compare the server and client image list
                for item in self.server_list:
                        if item in self.client_list:
                            pass
                        else:
                            self.server_connection.request('GET', '/img/{}'.format(item.replace(' ', '%20')))
                            with open(CLIENT_DIR + "{}".format(item.replace('%20',' ')),'wb') as f:
                                f.write(self.server_connection.getresponse().read())
                                print('Added {}'.format(item))
                            self.server_connection.close()
                            self.client_list.append(item)
                return True
            except Exception as err:
                #Handles error and resets the connection
                self.clientExceptionHandler(err)
                self.server_connection = http.client.HTTPConnection(self.server_ip, PORT)
                return False

        def clientExceptionHandler(self,err):
                print(type(err).__name__)
                if isinstance(err, http.client.RemoteDisconnected) or (isinstance(err, http.client.NotConnected)) or isinstance(err,http.client.CannotSendRequest):
                    logging.error("Resetting connection with the Server. The error is {}".format(type(err).__name__))
                    self.server_connection.close()
                elif isinstance(err, http.client.IncompleteRead):
                    logging.error("Lost connection while downloading a file.")
                elif isinstance(err, TimeoutError):
                    logging.error("Server didn't respond. Check server activity!")
                elif isinstance(err, ConnectionRefusedError):
                    logging.error("Server is refusing connection.")
                else:
                    logging.error(str(type(err).__name__))