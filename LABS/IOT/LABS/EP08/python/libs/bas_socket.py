import socket

def socketListener(in_serverip , in_port , in_buffsize=4096):
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    server.bind((in_serverip,in_port))
    server.listen(1)
    print('Listening Income Request....')

    client, addr = server.accept()
    print('connected from:', addr)

    data = client.recv(in_buffsize).decode('utf-8')
    print(data)
    client.send('received your messages.'.encode('utf-8'))
    client.close()

    return data

def socketSendData(in_serverip , in_port , in_meassage , in_buffsize=4096):
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    server.connect((in_serverip,in_port))
    server.send(in_meassage.encode('utf-8'))
    data_server = server.recv(in_buffsize).decode('utf-8')
    print('Server:' , data_server)
    server.close()
    return data_server
'''
def displayTemperature():
    #####################
    serverip = '192.168.1.37'
    port = 9008
    #####################

    buffsize = 4096

    while True:
            server = socket.socket()
            server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
            server.bind((serverip,port))
            server.listen(1)
            print('waiting micropython...')

            client, addr = server.accept()
            print('connected from:', addr)

            data = client.recv(buffsize).decode('utf-8')
            print('Data from MicroPython: ',data) 
            #data_temp = data.split('|')[0]
            #data_humi = data.split('|')[1]
            data_temp = data.split('|')[0].split(':')
            data_humi = data.split('|')[1].split(':')

            if float(data_temp[1]) > 30:
                img = PhotoImage(file='level3.png')
                ICON.configure(image=img)
                ICON.image = img
                v_status.set('{} อุณหภูมิ {} ความชื้น {}'.format(data_temp[0],data_temp[1],data_humi[1]))
            elif float(data_temp[1]) > 27.5:
                img = PhotoImage(file='level2.png')
                ICON.configure(image=img)
                ICON.image = img
                v_status.set('{} อุณหภูมิ {} ความชื้น {}'.format(data_temp[0],data_temp[1],data_humi[1]))
            elif float(data_temp[1]) > 25.1:
                img = PhotoImage(file='level1.png')
                ICON.configure(image=img)
                ICON.image = img
                v_status.set('{} อุณหภูมิ {} ความชื้น {}'.format(data_temp[0],data_temp[1],data_humi[1]))
            else:
                img = PhotoImage(file='level1.png')
                ICON.configure(image=img)
                ICON.image = img
                v_status.set('อุณหภูมิเย็นเกินไป ความชื้น {}'.format(data_humi[1])) 
                
            client.send('received your messages.'.encode('utf-8'))
            client.close()
'''          