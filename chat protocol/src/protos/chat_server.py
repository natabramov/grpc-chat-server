from concurrent import futures

import logging

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

from chat_pb2_grpc import ChatServerServicer
import chat_pb2_grpc

import time


class ChatServer(ChatServerServicer):

    def __init__(self) -> None:
        self._channelMessages = {}
        self._channelUserList = {}
        self._channelOwners = {}

    def _get_timestamp(self) -> int:
        return int(time.time())

    def _print_debug_entry(self, request) -> None:
        print(
            f"Handling send message request for channel {request.channel} from user {request.user.name}")

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

        return response

    def Channel_MemberUpdate(
            self,
            request: ChannelMemberUpdateRequest,
            context) -> GenericResponse:

        self._print_debug_entry(request)

        if request.channel not in self._channelUserList:
            self._channelUserList[request.channel] = []

        if request.type == "Join" and request.user not in self._channelUserList[
                request.channel]:
            print(
                f"User {request.user.name} has joined channel {request.channel}")
            self._channelUserList[request.channel].append(request.user)

        elif request.type == "Leave" and request.user in self._channelUserList[request.channel]:
            print(
                f"User {request.user.name} has left channel {request.channel}")
            self._channelUserList[request.channel].remove(request.user)

        return GenericResponse(
            successful=True,
            timestamp=self._get_timestamp())

    def Channel_Create(self,
                       request: ChannelCreateRequest,
                       context) -> GenericResponse:

        new_channel = Channel(topic=ChannelCreateRequest.channelname,
                              users=ChannelCreateRequest.user)

        successful = True
        if new_channel not in self._channelOwners:
            print(
                f"User {request.user.name} has created channel {request.channel}")
            self._channelOwners[new_channel] = request.user
        else:
            print(
                f"User {request.user.name} has tried to create channel {request.channel} but it already exists")
            successful = False

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

        return GenericResponse(
            successful=successful,
            timestamp=self._get_timestamp())


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chat_pb2_grpc.add_ChatServerServicer_to_server(ChatServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
