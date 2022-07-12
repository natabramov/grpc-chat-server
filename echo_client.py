import socket

HEADER = 20
HOST = "127.0.0.1"
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    
    sent_msg = s.sendall(b'hi') #msg in byte form
    data = s.recv(1024)
    print(f"Received {data!r}")

    msg = b'hi'
    message = msg.decode('utf-8') #makes msg string
    msg_length = len(message)  #gets length/size of msg

    send_length = str(msg_length).encode('utf-8')   #send length is initially the size of the msg
    #send_length += b' ' * (HEADER - len(send_length)) #creates spaces to make fillers so first msg is size of header 

    s.sendall(send_length) #sends size of outgoing message
    data = s.recv(1024)

    print(f"Received {data!r}")

    s.sendall(msg) #sends message
    data = s.recv(1024)

    print(f"Received {data!r}")