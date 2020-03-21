# Hypertext Transfer Protocol - HTTP
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET https://www.py4e.com/lessons/network HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    #print(data.decode(),end='')

mysock.close()




# Retrieving web pages with urllib
import urllib.request

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    # print(line.decode().strip())



# compute the frequency of each word
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('https://stackoverflow.com')

counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)