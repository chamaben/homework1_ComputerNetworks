import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT)) #bind socket to address
    s.listen() #Enable a server to accept connections
    #get socket, return address
    conn, addr = s.accept() #
    with conn:
        print(f"Server connected to {addr}")
        while True:
            # receive data from socket:
            data = conn.recv(128)
            if not data:
                break
            # print received data
            print(f"Received {data!r}")
            # send data to socket:
            conn.sendall(data)