import socket

HEADER = 20
HOST = "127.0.0.1"
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    
    msg = "hiii"
    message = msg.encode('utf-8') #makes msg string
    msg_length = len(message).to_bytes(2, byteorder= 'big')   #gets length/size of msg
    #send_length = str(msg_length).encode('utf-8')   #send length is initially the size of the msg
    #send_length += b' ' * (HEADER - len(send_length)) #creates spaces to make initial 

    s.send(msg_length)
    data = s.recv(1024)

    print(f"Received {data!r}")

    s.send(message)
    data = s.recv(1024)

    print(f"Received {data!r}")