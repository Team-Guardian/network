import http.client
import sys
import os
import threading, time
import queue
from settings import PORT

class _client_list(object):

        def __init__(self):
            self.client_list = []
            self.server_list = []
            self.waiting_list = queue.Queue()
            self.port = PORT
            self.server_list_lock = threading.Lock()
            self.islocked = False
            self.is_wait_listed = False
            self.server_ip = "localhost"
            self.server_connection = http.client.HTTPConnection(self.server_ip, PORT)
            self.initial_client_list_created = False

        def request_server(self):

            # server_connection = http.client.HTTPConnection(server_ip, PORT)
             self.server_connection.connect()


             if (self.islocked == False) and (self.is_wait_listed == False):
              # Get server directory list
                  self.server_connection.request('GET', '/img/')
                  self.server_list = self.server_connection.getresponse().read()
                  self.server_list_lock.acquire()
                  print('server list is locked now')
                  self.server_list = self.server_list.splitlines()

                  print('Server Image list:')
                  print(self.server_list)

                  # Decoding server list
                  for item in range(self.server_list.__len__()):
                      b = self.server_list[item]
                      b = b.decode("utf-8")
                      self.server_list[item] = b

                  self.islocked = True
                  print('Decoded Server list:')
                  print(self.server_list)
             elif (self.islocked == True) and (self.is_wait_listed == False):
                self.server_connection.request('GET', '/img/')
                self.waiting_list.put(self.server_connection.getresponse().read())
                self.is_wait_listed = True
             elif (self.islocked == False) and (self.is_wait_listed == True):
                 del self.server_list [:]
                 self.server_list = []
                 for i in range(self.waiting_list.qsize):
                      self.server_list.append(self.waiting_list.get())
                 self.is_wait_listed = False
                 self.islocked=True

        def updating_client_list(self):

            if self.initial_client_list_created == False:

                # create a directory list for client
                for root, dirs, files in os.walk(r'C:/Users/Junaid Khan/Desktop'):
                    for file in files:
                        if file.endswith('.jpg'):
                            self.client_list.append(file)
                    self.initial_client_list_created =True


            print('Original Client list:')
            print(self.client_list)


         # compare the server and client image list
            if (self.islocked == True) and (self.is_wait_listed == False):
                for item in self.server_list:
                    if item in self.client_list:
                        pass
                    else:
                        self.server_connection.request('GET', '/img/{}'.format(item))
                        with open("{}".format(item),'wb') as f:
                            f.write(self.server_connection.getresponse().read())
                            print('Added {}'.format(item))
                        f.close()
                self.islocked = False
                self.server_list_lock.release()

            # Append the new images to the client's directory
                del self.client_list [:]

                for root, dirs, files in os.walk(r'C:/Users/Junaid Khan/Desktop'):
                    for file in files:
                         if file.endswith('.jpg'):
                            self.client_list.append(file)

                print('Updated Client list:')
                print(self.client_list)



if __name__ == "__main__":


    client_list = _client_list()

    thread1 = threading.Thread(target=client_list.request_server())
    thread2 = threading.Thread(target=client_list.updating_client_list())
    thread1.start()
    thread2.start()

    while True:
        client_list.request_server()
        client_list.updating_client_list()
        print('In here')
        time.sleep(10)


























