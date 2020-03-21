# This is using HTTP 1.0 - not all servers support the oldest protocol
# Try http://data.pr4e.org/romeo.txt if your server fails.
# 전혀 해결 안된 문제임!

import socket
import urllib

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET https://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

url = input('Enter: ')
try:

    fhand = urllib.request.urlopen(url)
    words = url.split('/')
    host = words[2]
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))
    mysock.send(('GET '+url+' HTTP/1.0\r\n\r\n').encode())


    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(),end=' ')
except:
    print('Non-existent URL')
    exit()

mysock.close()