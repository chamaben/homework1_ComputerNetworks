import socket

HOST = "127.0.0.1"  # The server's IP address
PORT = 12345  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock: # create socket object
    sock.connect((HOST, PORT)) # connect to server
    sock.sendall(b"Client is here.") # send message
    data = sock.recv(1024) # read servers reply

print(f"Received {data!r}") # print reply from server