import socket

HEADER = 20
HOST = "127.0.0.1"
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    connection, address = s.accept()
    with connection:
        print(f"Connected by {address}")
        while True:
            msg_length = int(connection.recv(HEADER).decode('utf-8'))
            msg_length = int(msg_length)
            data = connection.recv(msg_length)
            if not data:
                break
            connection.sendall(data)