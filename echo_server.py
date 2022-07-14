import socket

HEADER = 4
HOST = "127.0.0.1"
PORT = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen()
print("Server is listening ... ")

while True:
    connection, address = s.accept()
    if connection:
        print(f"Connected by [{address}]")

        while True:
            msg_length = connection.recv(HEADER) #reads the data in byte form, length of message
            msg_length = int.from_bytes(msg_length, "big") #converts bytes into integer to get the length of the message
            data = connection.recv(msg_length) #reads the message using the message length found
            connection.sendall(data)
            if data.lower() == b"bye":
                break
        print(f"\n[{address}] has disconnected. Awaiting another connection...")
    else:
        s.listen()
        print("Server is listening ... ")