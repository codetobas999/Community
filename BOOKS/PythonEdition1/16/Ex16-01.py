import socket

s = socket.socket()
host = "127.0.0.1"
port = 5000
print("server IP:", host)
print("... waiting connection request from client ...")
s.bind((host, port))
s.listen(5)
while True:
    c, addr = s.accept()
    print("... get connection from client ...")
    while True:
        sdata = input("server >>> ")
        c.send(str.encode(sdata))
        if str(sdata) == "BYE":
            check = 0
            c.close()
            break
        else:
            rdata = c.recv(1024)
            rdata = bytes.decode(rdata)
            print("client >>> ",  rdata)
    if check == 0:
        s.close()
        break
