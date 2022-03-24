# Network - Sockets - Examples sockets
#---------------------------------------------------------------------
# 24-Mar-22 - Warm up
# print("hello world")
# filename = input("enter file name")
# if(len(filename)>0):
#     print(filename)
#---------------------------------------------------------------------
# Retrieveing plain text - https://rosettacode.org/wiki/Hello_world/Web_server
# import socket

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# #mysock.connect(('data.pr4e.org', 80))
# mysock.connect(('google.com', 80))
# #cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# cmd = 'GET https://www.google.com/help.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)

# while True:
#     data = mysock.recv(512)
#     if (len(data) < 1):
#         break
#     print(data.decode())
# mysock.close()

#---------------------------------------------------------------------
# Retrieving image
# import socket
# import time

# HOST = 'data.pr4e.org'
# PORT = 80
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect((HOST, PORT))
# mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
# count = 0
# picture = b""

# while True:
#     data = mysock.recv(5120)
#     if (len(data) < 1): break
#     time.sleep(0.25)
#     count = count + len(data)
#     print(len(data), count)
#     picture = picture + data

# mysock.close()
#--------------------------------------------------------------------------------
