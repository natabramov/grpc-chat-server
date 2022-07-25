from concurrent import futures

import logging

import grpc

from chat_pb2 import GenericResponse
from chat_pb2 import ChannelGetMessagesRequest
from chat_pb2 import ChannelGetMessagesResponse
from chat_pb2 import ChannelMessage
from chat_pb2 import ChannelMemberUpdateRequest
from chat_pb2 import ChannelSendMessageRequest

from chat_pb2_grpc import ChatServerServicer
import chat_pb2_grpc

import time

class ChatServer(ChatServerServicer):

    def __init__(self) -> None:
        self._channelMessages = {}
        
    def _get_timestamp(self) -> int:
        return int(time.time())

    def _print_debug_entry(self, request) -> None:
        logging.debug("Handling send message request for channel %s from user %s",
            request.channel, request.user.name)

    def _extract_message(self, request: ChannelSendMessageRequest) -> ChannelMessage:
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

        self._channelMessages[request.channel].append(self._extract_message(request))

        return GenericResponse(successful=True, timestamp=self._get_timestamp())

    def Channel_GetMessages(
        self,
        request: ChannelGetMessagesRequest,
        context) -> ChannelGetMessagesResponse:

        self._print_debug_entry(request)

        results = None
        successful = False
        if request.channel in self._channelMessages:
            results = filter(lambda message: message.timestamp >= request.since, self._channelMessages[request.channel])
            successful = True

        response = ChannelGetMessagesResponse(
            successful=successful,
            timestamp=self._get_timestamp())
        response.messages.extend(results)

        return response

    def Channel_MemberUpdate(
        self,
        request: ChannelMemberUpdateRequest,
        context) -> GenericResponse:

        self._print_debug_entry(request)

        return GenericResponse(successful=True, timestamp=self._get_timestamp())

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chat_pb2_grpc.add_ChatServerServicer_to_server(ChatServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()