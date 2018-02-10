import http.client
import sys

#server_ip = sys.argv[1]

server_ip = "142.58.209.9"
server_connection = http.client.HTTPConnection(server_ip,9999)
server_connection.connect()
server_connection.request('GET','/img/')
server_list = server_connection.getresponse().read()

server_list = server_list.splitlines()

#z is the server image list copy
client_list = open('imgs-listing.txt','r').read()

print('Server Image list:')
print(server_list)

for item in range(server_list.__len__()):
    b = server_list[item]
    b = b.decode("utf-8")
    server_list[item]=b

print('The decoded list is:')
print(server_list)
print('Client Image list:')
print(client_list)

#compare the server and client image list


for item in server_list:
    if item in client_list:
        pass
    else:
        server_connection.request('GET', '/img/{}'.format(item))
        with open("{}".format(item),'wb') as f:
            f.write(server_connection.getresponse().read())
        f.close()







