import socket
import threading
import logging

HEADER = 16
HOST = "127.0.0.1"
PORT = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen()
print("Server is listening ... ")

def established_conn(conn):
    format = "[%(asctime)s] %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info(f"Connected by [{address}]")

    while True:
        msg_length = conn.recv(HEADER) #reads the data in byte form, length of message
        msg_length = int.from_bytes(msg_length, "big") #converts bytes into integer to get the length of the message
        data = conn.recv(msg_length) #reads the message using the message length found
        conn.sendall(data)
        if data.lower() == b"bye":
            break
    logging.info(f"[{address}] has disconnected. Awaiting another connection...")

while True:
    connection, address = s.accept()
    if connection:
        thread = threading.Thread(target=established_conn, args=(connection, ))
        thread.start()
    else:
        s.listen()
        print("Server is listening ... ")