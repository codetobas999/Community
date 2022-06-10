import socket

s = socket.socket()
host = "127.0.0.1"
port = 5000
print("server IP:", host)
print("... request connection to server ...")
s.connect((host, port))
while True:
    sdata = s.recv(1024)
    sdata = bytes.decode(sdata)
    print("server >>> ", sdata)
    if sdata == "BYE":
        s.close()
        break
    else:
        sdata = input("client >>> ")
        s.send(str.encode(sdata))
