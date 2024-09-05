import socket
import hashlib

s = socket.socket()

port = 12346

s.connect(('127.0.0.1', port))

s.send("hello".encode())

resp = s.recv(1024)
m = hashlib.sha256()
m.update("hello".encode())
s.close()
if  resp == m.digest() :
    print("message integrity preserved")
else :
    print("message integrity not preserved")
