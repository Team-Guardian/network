import http.client
import sys
import os
import time
from settings import PORT, CLIENT_DIR


class _client_list(object):

        def __init__(self):
            self.client_list = []
            self.server_list = []
            self.port = PORT
            self.server_ip = "localhost" #sys.argv[1]
            self.server_connection = http.client.HTTPConnection(self.server_ip, PORT)
            self.initial_client_list_created = False

        def request_server(self):

              #Get server directory list
              self.server_connection.request('GET', '/img/')
              self.server_list = self.server_connection.getresponse().read()
              self.server_list = self.server_list.splitlines()

              print('Server Image list:')
              print(self.server_list)

              #Decoding server list
              for item in range(self.server_list.__len__()):
                  b = self.server_list[item]
                  b = b.decode("utf-8")
                  self.server_list[item] = b

              print('Decoded Server list:')
              print(self.server_list)

        def updating_client_list(self):

            if self.initial_client_list_created == False:

                #create a directory list for client
                for root, dirs, files in os.walk(CLIENT_DIR):
                    for file in files:
                        if file.endswith('.jpg'):
                            self.client_list.append(file)
                    self.initial_client_list_created =True

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

           #Append the new images to the client's directory
            del self.client_list [:]

            for root, dirs, files in os.walk(CLIENT_DIR):
                for file in files:
                     if file.endswith('.jpg'):
                        self.client_list.append(file)

            print('Updated Client list:')
            print(self.client_list)


if __name__ == "__main__":

    client_list = _client_list()

    while True:
        client_list.request_server()
        client_list.updating_client_list()
        time.sleep(0.2)

























