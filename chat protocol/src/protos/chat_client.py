from __future__ import print_function

import logging

import grpc
import chat_pb2
import chat_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = chat_pb2_grpc.ChatServerStub(channel)
        response = stub.SendChat(chat_pb2.ChatRequest(username='Natalie'))
        print(response.successful)
        response2 = stub.JoinChannel(chat_pb2.JoinRequest(username='Natalie'))
        print(response2.successful)
        response3 = stub.LeaveChannel(chat_pb2.LeaveRequest(username='Natalie'))
        print(response3.successful)
if __name__ == '__main__':
    logging.basicConfig()
    run()
