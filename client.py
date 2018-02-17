import http.client
import sys
import os
import time
from settings import PORT, CLIENT_DIR


class Client(object):

        def __init__(self):
            self.client_list = []
            self.server_list = []
            self.port = PORT
            self.server_ip = "localhost" #sys.argv[1]
            self.server_connection = http.client.HTTPConnection(self.server_ip, PORT)
            self.initial_client_list_created = False
            for file in os.listdir(CLIENT_DIR):
                if file.endswith('.jpg'):
                    self.client_list.append(file)



        def requestServer(self):

              #Get server directory list
              self.server_connection.request('GET', '/img/')
              self.server_list = self.server_connection.getresponse().read().decode("utf-8").splitlines()

              print('Server Image list:')
              print(self.server_list)

              print('Decoded Server list:')
              print(self.server_list)

        def updateClientList(self):

            print('Original Client list:')
            print(self.client_list)

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

            print('Updated Client list:')
            print(self.client_list)


if __name__ == "__main__":

    client = Client()

    while True:
        client.requestServer()
        client.updateClientList()
        time.sleep(0.2)

