from __future__ import print_function

import logging

import grpc
import chat_pb2
import chat_pb2_grpc

import time

def get_auth_user():
    return chat_pb2.AuthUser(
        name='natabr',
        token='doesnt exist yet')

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = chat_pb2_grpc.ChatServerStub(channel)

        timestamp = int(time.time())

        status = stub.Status(chat_pb2.Empty())
        print('status: ', status.successful)

        # Create account
        response1 = stub.Account_Create(chat_pb2.AccountCreateRequest(
            username='fatcat',
            password='hello123',
            timestamp=timestamp))
        print('created account natabr: ', response1.successful)
        status1 = stub.Status(chat_pb2.Empty())
        print('status1: ', status1.successful)

        # Create channel
        response2 = stub.Channel_Create(chat_pb2.ChannelCreateRequest(
            user=get_auth_user(),
            channelname='testchannel',
            timestamp=timestamp))
        print('created channel testchannel: ', response2.successful)
        status2 = stub.Status(chat_pb2.Empty())
        print('status2: ', status2.successful)

        # Join channel
        response3 = stub.Channel_MemberUpdate(chat_pb2.ChannelMemberUpdateRequest(
            user=get_auth_user(),
            channel='testchannel',
            type=chat_pb2.ChannelMemberUpdateRequest.UpdateType.Join))
        print('authuser natabr created channel testchannel: ', response3.successful)
        status3 = stub.Status(chat_pb2.Empty())
        print('status3: ', status3.successful)

        # Create account 2
        response4 = stub.Account_Create(chat_pb2.AccountCreateRequest(
            username='bananakitty',
            password='kiwi55!',
            timestamp=timestamp))
        print('create account fatcat: ', response4.successful)
        status4 = stub.Status(chat_pb2.Empty())
        print('status4: ', status4.successful)

        # Join channel 2
        response6 = stub.Channel_MemberUpdate(chat_pb2.ChannelMemberUpdateRequest(
            user=chat_pb2.AuthUser(name='fatcat',token='not created yet'),
            channel='testchannel',
            type=chat_pb2.ChannelMemberUpdateRequest.UpdateType.Join))
        print('fatcat join testchannel: ', response6.successful)
        status6 = stub.Status(chat_pb2.Empty())
        print('status6: ', status6.successful)

        # Say a message
        message = chat_pb2.ChatMessage(
            text='hello')
            
        response7 = stub.Channel_SendMessage(chat_pb2.ChannelSendMessageRequest(
            user=get_auth_user(),
            channel='testchannel',
            chat=message,
            timestamp=timestamp))
        print('natabr send message hello: ', response7.successful)
        status7 = stub.Status(chat_pb2.Empty())
        print('status7: ', status7.successful)

        # Read messages
        response8 = stub.Channel_GetMessages(chat_pb2.ChannelGetMessagesRequest(
            user=get_auth_user(),
            channel='testchannel',
            since=timestamp))
        for message in response8.messages:
            print(message.user + ": " + message.chat.text)
        status8 = stub.Status(chat_pb2.Empty())
        print('status8: ', status8.successful)

        # Leave channel
        response9 = stub.Channel_MemberUpdate(chat_pb2.ChannelMemberUpdateRequest(
            user=get_auth_user(),
            channel='testchannel',
            password=None,
            type=chat_pb2.ChannelMemberUpdateRequest.UpdateType.Leave))
        print('natabr leave channel: ', response9.successful)
        status9 = stub.Status(chat_pb2.Empty())
        print('status9: ', status9.successful)

        # Delete account
        response10 = stub.Account_Delete(chat_pb2.AccountDeleteRequest(
            user=chat_pb2.AuthUser(name='fatcat',token='not created yet'),
            password='kiwi55!',
            timestamp=timestamp))
        print('fatcat delete account: ', response10.successful)
        status10 = stub.Status(chat_pb2.Empty())
        print('status10: ', status10.successful)    

if __name__ == '__main__':
    logging.basicConfig()
    run()