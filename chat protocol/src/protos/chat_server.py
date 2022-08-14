from concurrent import futures

import logging
from typing import Generic

import grpc

from chat_pb2 import GenericResponse
from chat_pb2 import ChannelCreateRequest
from chat_pb2 import ChannelDeleteRequest
from chat_pb2 import ChannelGetMessagesRequest
from chat_pb2 import ChannelGetMessagesResponse
from chat_pb2 import ChannelMessage
from chat_pb2 import ChannelMemberUpdateRequest
from chat_pb2 import ChannelSendMessageRequest
from chat_pb2 import Channel
from chat_pb2 import AccountCreateRequest
from chat_pb2 import AccountDeleteRequest
from chat_pb2 import LoginRequest
from chat_pb2 import AuthUser
from chat_pb2 import Empty

from chat_pb2_grpc import ChatServerServicer
import chat_pb2_grpc

import time

from chat_pb2 import Account


class ChatServer(ChatServerServicer):

    def __init__(self) -> None:
        self._channelMessages = {}
        self._channelUserList = {}
        self._channelOwners = {}
        self._accounts = {}
        self._accountstatus = {}

    def _get_timestamp(self) -> int:
        return int(time.time())

    def _print_debug_entry(self, request) -> None:
        print(
            f"Handling send message request for channel {request.channel} from user {request.user.name}")

    def Status(self,
               request: Empty,
               context):
               
        print('\n,','self._channelMessages: ', self._channelMessages,'\n',
              'self._channelUserList: ', self._channelUserList, '\n',
              'self._channelOwners: ', self._channelOwners, '\n',
              'self._accounts: ', self._accounts, '\n',
              'self._accountstatus: ', self._accountstatus)

        return GenericResponse(
            successful=True,
            timestamp=self._get_timestamp())

    def _extract_message(
            self,
            request: ChannelSendMessageRequest) -> ChannelMessage:
        channel_message = ChannelMessage(
            user=request.user.name,
            timestamp=request.timestamp)

        if request.HasField("chat"):
            channel_message.chat.CopyFrom(request.chat)
        elif request.HasField("image"):
            channel_message.image.CopyFrom(request.image)

        #self.Status()
        return channel_message

    def Channel_SendMessage(
            self,
            request: ChannelSendMessageRequest,
            context) -> GenericResponse:

        self._print_debug_entry(request)

        if request.channel not in self._channelMessages:
            self._channelMessages[request.channel] = []

        print(
            f"Adding message to channel {request.channel} from user {request.user.name}")
        self._channelMessages[request.channel].append(
            self._extract_message(request))
        #self.Status()
        return GenericResponse(
            successful=True,
            timestamp=self._get_timestamp())

    def Channel_GetMessages(
            self,
            request: ChannelGetMessagesRequest,
            context) -> ChannelGetMessagesResponse:

        self._print_debug_entry(request)

        results = []
        successful = False
        if request.channel in self._channelMessages:
            results = filter(lambda message: message.timestamp >=
                             request.since, self._channelMessages[request.channel])
            successful = True

        response = ChannelGetMessagesResponse(
            successful=successful,
            timestamp=self._get_timestamp())
        response.messages.extend(results)

        print(
            f"User {request.user.name} requested messages since {request.since}. Returning {len(response.messages)} messages")
        #self.Status()
        return response

    def Channel_MemberUpdate(
            self,
            request: ChannelMemberUpdateRequest,
            context) -> GenericResponse:

        self._print_debug_entry(request)

        if request.channel not in self._channelUserList:
            self._channelUserList[request.channel] = []

        if request.type == ChannelMemberUpdateRequest.Join and request.user not in self._channelUserList[
                request.channel]:
            print(
                f"User {request.user.name} has joined channel {request.channel}")
            self._channelUserList[request.channel].append(request.user)

        elif request.type == ChannelMemberUpdateRequest.Join and request.user in self._channelUserList[request.channel]:
            print(
                f"User {request.user.name} has left channel {request.channel}")
            self._channelUserList[request.channel].remove(request.user)
        #self.Status()
        return GenericResponse(
            successful=True,
            timestamp=self._get_timestamp())

    def Channel_Create(self,
                       request: ChannelCreateRequest,
                       context) -> GenericResponse:

        successful = True
        if request.channelname not in self._channelOwners:
            print(
                f"User {request.user.name} has created channel {request.channelname}")
            self._channelOwners[request.channelname] = request.user
        else:
            print(
                f"User {request.user.name} has tried to create channel {request.channelname} but it already exists")
            successful = False
        #self.Status()
        return GenericResponse(
            successful=successful,
            timestamp=self._get_timestamp())

    def Channel_Delete(self,
                       request: ChannelDeleteRequest,
                       context) -> GenericResponse:

        successful = True
        if self._channelOwners[request.channel] == request.user:
            print(
                f"User {request.user.name} has deleted channel {request.channel}")
            del self._channelUserList[request.channel]
            del self._channelOwners[request.channel]
            del self._channelMessages[request.channel]
        else:
            print(
                f"User {request.user.name} has tried to delete channel {request.channel} but they aren't allowed to")
            successful = False
        #self.Status()
        return GenericResponse(
            successful=successful,
            timestamp=self._get_timestamp())

    def Account_Create(self,
                       request: AccountCreateRequest,
                       context) -> GenericResponse:
        
        new_account = Account(username=request.username,
                              password=request.password)

        successful = True
        if new_account.username not in self._accounts:
            print(
                f"Account {request.username} has been created")
            self._accounts[request.username] = request.password
            self._accountstatus[request.username] = False #not logged in yet
        else:
            print(
                f"Username {request.username} already exists")
            successful = False

        return GenericResponse(
            successful=successful,
            timestamp=self._get_timestamp())

    def Account_Delete(self,
                       request: AccountDeleteRequest,
                       context) -> GenericResponse:

        successful = True

        if self._accounts[request.username] == request.password:
            print(
                f"User {request.username} has deleted their account")
            del self._accounts[request.username]

        else:
            print(
                f"User {request.username} has tried to delete their account but the password is incorrect")
            successful = False
        
        return GenericResponse(
            successful=successful,
            timestamp=self._get_timestamp())
        
    def Login(self,
              request: LoginRequest,
              context) -> AuthUser or GenericResponse:
        
        if request.password == self._accounts[request.username]:
            self._accountstatus[request.username] = True #user is logged in
            return AuthUser(name = request.username,
                            token = 'not created yet')

        else:
            return AuthUser(name = request.username,
                            token = 'invalid')

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chat_pb2_grpc.add_ChatServerServicer_to_server(ChatServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()