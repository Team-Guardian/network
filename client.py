import http.client
import sys

server_ip = sys.argv[1]
#server_ip = "127.0.1.10"
x = http.client.HTTPConnection(server_ip, 9999)
x.connect()
x.request('GET', '/img/imgs-listen.txt')
y = x.getresponse()
z = y.read()
print(z)