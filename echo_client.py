import socket

HEADER = 20
HOST = "127.0.0.1"
PORT = 12345
user_input = 'hi'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    
    print("[Type 'Bye' to disconnect]")
    while user_input.lower() != 'bye'.lower():
        user_input = input("\nType a message: ")
        
        msg = user_input.encode('utf-8') #makes a str
        send_length = len(msg).to_bytes(4, "big") #converts str to bytes

        s.sendall(send_length) #sends size of outgoing message to server
        s.sendall(msg) #sends msg to server 
        data = s.recv(1024)

        print(f"Received {data!r}")




    # msg = 'hi'.encode('utf-8') #makes a str
    # send_length = len(msg).to_bytes(4, "big") #converts str to bytes

    # s.sendall(send_length) #sends size of outgoing message to server
    # s.sendall(msg) #sends msg to server 
    # data = s.recv(1024)

    # print(f"Received {data!r}")

    # ###

    # msg2 = 'BYE'.encode('utf-8')
    # send_length2 = len(msg2).to_bytes(4, "big")

    # s.sendall(send_length2)
    # s.sendall(msg2)
    # data2 = s.recv(1024)

    # print(f"Received {data2!r}")
