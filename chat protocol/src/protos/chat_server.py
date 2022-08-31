from concurrent import futures

import logging
from sqlite3 import IntegrityError
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
from chat_pb2 import Account

from chat_pb2_grpc import ChatServerServicer
import chat_pb2_grpc

import time

from database import create_connection
from database import create_cred
from database import delete_cred
from database import read_cred
from database import read_channel_owner
from database import create_channel_owner
from database import delete_channel_owner
from database import add_account_status
from database import update_account_status
from database import delete_account_status

class ChatServer(ChatServerServicer):

    def __init__(self) -> None:
        self._channelMessages = {}
        self._channelUserList = {}
        self._channelOwners = {}
        #self._accounts = {}
        self._accountstatus = {}
        self._dbpath = r"..\..\..\..\\summer-project\sqlite\db\pythonsqlite2.db"

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
              'self._channelOwners: ', self._channelOwners, '\n')
              #'self._accountstatus: ', self._accountstatus

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

        conn = create_connection(self._dbpath)
        cred = (request.channelname, request.user.name, request.password)

        successful = True
        if not read_channel_owner(conn, cred):
            print(
                f"User {request.user.name} has created channel {request.channelname}")
            #self._channelOwners[request.channelname] = request.user
            try:
                create_channel_owner(conn, cred)
            except IntegrityError:
                print(
                    f"User {request.user.name} has tried to create channel {request.channelname} but it already exists")
                successful = False
        # might need to remove the else
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

        conn = create_connection(self._dbpath)
        cred = (request.channel, request.user.name, request.password)

        successful = True
        #if self._channelOwners[request.channel] == request.user:
        try:
            if read_channel_owner(conn, cred)[0][0] == request.channel and read_channel_owner(conn, cred)[0][1] == request.user.name and read_channel_owner(conn, cred)[0][2] == request.password:
                print(
                    f"User {request.user.name} has deleted channel {request.channel}")
                    #del self._accounts[request.username]
                delete_channel_owner(conn, cred)

        except TypeError:
            print(
                f"User {request.user.name} has tried to delete channel {request.channel} but they aren't allowed to")

        return GenericResponse(
            successful=successful,
            timestamp=self._get_timestamp())

    def Account_Create(self,
                       request: AccountCreateRequest,
                       context) -> GenericResponse:
        
        new_account = Account(username=request.username,
                              password=request.password)


        conn = create_connection(self._dbpath)
        cred = (request.username, request.password)

        successful = True
        if not read_cred(conn, cred):
            print(
                f"Account {request.username} has been created")
            #self._accounts[request.username] = request.password
            #self._accountstatus[request.username] = False #not logged in yet
            add_account_status(conn, (request.username, 0))
            try:
                create_cred(conn, cred)
            except IntegrityError:
                print(
                    f"Username {request.username} already exists")
                successful = False
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

        conn = create_connection(self._dbpath)
        cred = (request.user.name, request.password)

        #if self._accounts[request.username] == request.password:
        try:
            if read_cred(conn, cred)[0][0] == request.user.name and read_cred(conn, cred)[0][1] == request.password:
                print(
                    f"User {request.user.name} has deleted their account")
                #del self._accounts[request.username]
                conn = create_connection(self._dbpath)
                delete_cred(conn, cred)
                delete_account_status(conn, cred)
        except (TypeError, IndexError) as e:
            print(
                f"User {request.user.name} has tried to delete their account but the username or password is incorrect")
            successful = False
        
        return GenericResponse(
            successful=successful,
            timestamp=self._get_timestamp())
        
    def Login(self,
              request: LoginRequest,
              context) -> AuthUser or GenericResponse:
        
        conn = create_connection(self._dbpath)
        cred = (request.username, request.password)

        db_credentials = read_cred(conn, cred)
        if db_credentials[0][0] == request.username and db_credentials[0][1] == request.password:
            update_account_status(conn, (request.username, 1))
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