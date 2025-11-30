# client
import socket

client_socket = socket.socket()

#connect to server
client_socket.connect(('localhost', 9999))
name = input()
client_socket.send(name.encode())
print(client_socket.recv(1024).decode())
client_socket.close()