import http.client
import sys
import os

server_ip = "localhost"

#server_ip = sys.argv[1]
server_connection = http.client.HTTPConnection(server_ip,9999)
server_connection.connect()
server_connection.request('GET','/img/')
server_list = server_connection.getresponse().read()

server_list = server_list.splitlines()

#create a directory list for client
client_list = []
for root, dirs, files in os.walk(r'C:/Users/Junaid Khan/Desktop'):
        for file in files:
            if file.endswith('.jpg'):
                client_list.append(file)

print('Original Client list:')
print(client_list)
#client_list = open('imgs-listing.txt','r').read()

print('Server Image list:')
print(server_list)

for item in range(server_list.__len__()):
    b = server_list[item]
    b = b.decode("utf-8")
    server_list[item]=b


print('Decoded list:')
print(server_list)

#compare the server and client image list

for item in server_list:
    if item in client_list:
        pass
    else:
        server_connection.request('GET', '/img/{}'.format(item))
        with open("{}".format(item),'wb') as f:
            f.write(server_connection.getresponse().read())
        f.close()

del client_list[:]

for root, dirs, files in os.walk(r'C:/Users/Junaid Khan/Desktop'):
        for file in files:
            if file.endswith('.jpg'):
                client_list.append(file)

print('Updated Client list:')
print(client_list)









