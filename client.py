#!/usr/bin/env python3

import socket, time

HOST = '172.16.52.35'  
PORT = 8080        

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        data = input("# ")
        s.sendall(data.encode())
        rec = s.recv(1024)
        if rec == True:
            print('Received: ', repr(data))


time.sleep(10)
