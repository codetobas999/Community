import socket

def send_data(serverip,port,data): 
    print('port : ' + str(port))
    server = socket.socket() 
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1) 
    server.connect((serverip,port)) 
    server.send(data.encode('utf-8')) 
    data_server = server.recv(1024).decode('utf-8')
    print('Server:' , data_server)
    server.close()