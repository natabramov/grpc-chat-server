import socket

HEADER = 20
HOST = "127.0.0.1"
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    
    msg = 'hi'.encode('utf-8')
    send_length = len(msg).to_bytes(4, "big")

    s.sendall(send_length) #sends size of outgoing message
    s.sendall(msg)
    data = s.recv(1024)

    print(f"Received {data!r}")

    ####

    msg2 = 'hello again'.encode('utf-8')
    send_length2 = len(msg2).to_bytes(4, "big")

    s.sendall(send_length2)
    s.sendall(msg2)
    data2 = s.recv(1024)

    print(f"Received {data2!r}")
