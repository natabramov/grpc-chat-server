import socket

HEADER = 20
HOST = "127.0.0.1"
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    
    sent_msg = s.sendall(b'hi') #msg in byte form
    data1 = s.recv(1024)
    print(f"Received {data1!r}")

    msg = b'hi'
    message = msg.decode('utf-8') #makes msg string
    msg_length = len(message)  #gets length/size of msg

    send_length = str(msg_length).encode('utf-8')   #send length is initially the size of the msg
    #send_length += b' ' * (HEADER - len(send_length)) #creates spaces to make fillers so first msg is size of header 

    s.sendall(send_length) #sends size of outgoing message
    data2 = s.recv(1024)

    print(f"Received {data2!r}")

    s.sendall(msg) #sends message
    data3 = s.recv(1024)

    print(f"Received {data3!r}")