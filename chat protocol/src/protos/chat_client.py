from __future__ import print_function

import logging

import grpc
import chat_pb2
import chat_pb2_grpc

import time

def get_auth_user():
    return chat_pb2.AuthUser(
        name='Natalie',
        token='doesnt exist yet')

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = chat_pb2_grpc.ChatServerStub(channel)

        timestamp = int(time.time())

        # Join channel
        response1 = stub.Channel_MemberUpdate(chat_pb2.ChannelMemberUpdateRequest(
            user=get_auth_user(),
            channel='testchannel',
            type=chat_pb2.ChannelMemberUpdateRequest.UpdateType.Join))
        
        print(response1.successful)

        # Say a message
        message = chat_pb2.ChatMessage(
            text='hello')
            
        response2 = stub.Channel_SendMessage(chat_pb2.ChannelSendMessageRequest(
            user=get_auth_user(),
            channel='testchannel',
            chat=message,
            timestamp=timestamp))

        print(response2.successful)

        # Read messages
        response3 = stub.Channel_GetMessages(chat_pb2.ChannelGetMessagesRequest(
            user=get_auth_user(),
            channel='testchannel',
            since=timestamp))

        for message in response3.messages:
            print(message.user + ": " + message.chat.text)
        
        # Leave channel
        response3 = stub.Channel_MemberUpdate(chat_pb2.ChannelMemberUpdateRequest(
            user=get_auth_user(),
            channel='testchannel',
            password=None,
            type=chat_pb2.ChannelMemberUpdateRequest.UpdateType.Leave))
        print(response3.successful)

if __name__ == '__main__':
    logging.basicConfig()
    run()
