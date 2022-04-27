import time
import socket
import sys
import os
s = socket.socket()
host = "192.168.1.19"
port = 8080
while True:
    if s.connect((host, port)) == 0:
        print("Connected to Server.")
    else:
        print("Not connected")
command = s.recv(1024)
command = command.decode()

if command == "open":
    print("Command is :", command)
    s.send("Command received".encode())
    os.system('ls')
