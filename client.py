import http.client
<<<<<<< Updated upstream
import sys

server_ip = sys.argv[1]
#server_ip = "127.0.1.10"
x = http.client.HTTPConnection(server_ip, 9999)
x.connect()
x.request('GET', '/img/imgs-listen.txt')
y = x.getresponse()
z = y.read()
print(z)
=======
import os
from Settings import PORT, CLIENT_DIR
import logging

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

        def requestServer(self):
              #Get server directory list
            try:
                self.server_connection.request('GET', '/img/')
                self.server_list = self.server_connection.getresponse().read().decode("utf-8").splitlines()
            except Exception as err:
                   self.clientExceptionHandler(err)

        def updateClientList(self):
            try:
                #Compare the server and client image list
                for item in self.server_list:
                        if item in self.client_list:
                            pass
                        else:
                            self.server_connection.request('GET', '/img/{}'.format(item))
                            with open("{}".format(item),'wb') as f:
                                f.write(self.server_connection.getresponse().read())
                                print('Added {}'.format(item))
                            f.close()
                            self.client_list.append(item)
            except Exception as err:
                self.clientExceptionHandler(err)

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
                    pass
>>>>>>> Stashed changes
