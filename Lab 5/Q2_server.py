import socket
import hashlib

s = socket.socket()
print ("Socket successfully created")

port = 12346
print ("socket binded to %s" %(port))


s.bind(('', port))
print ("socket binded to %s" %(port))

s.listen(5)
print ("socket is listening")
print ("socket binded to %s" %(port))

while True:
    c, addr = s.accept()
    print ('Got connection from', addr )
    msg = c.recv(1024)
    print(msg.decode())
    m = hashlib.sha256()
    m.update(msg)
    c.send(m.digest())
    c.close()
    break
