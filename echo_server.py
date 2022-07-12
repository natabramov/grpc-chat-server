import socket

HEADER = 4
HOST = "127.0.0.1"
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    connection, address = s.accept()
    with connection:
        print(f"Connected by {address}")
        while True:
            msg_length = connection.recv(HEADER) #reads the data in byte form, length of message
            msg_length = int.from_bytes(msg_length, "big")
            data = connection.recv(msg_length) #reads the message using the message length found
            if not data:
                break
            connection.sendall(data)