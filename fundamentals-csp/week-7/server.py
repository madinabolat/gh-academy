# server
import socket

#create socket
#by default - uses IP v4, TCP protocol
server_socket = socket.socket()
print("Server created")

#bind socket
#configure ip address and port
server_socket.bind(('localhost',9999))
print("Server bound")

#Server listens to connections
server_socket.listen(3)

while True:
    #server accepts new connections 
    #we save it to c, addr
    c, addr = server_socket.accept()
    c.send("Welcome to server".encode())
    name = c.recv(1024).decode('utf-8')
    print(f"Connection received from {name} at {addr}...")
    c.close()
    break