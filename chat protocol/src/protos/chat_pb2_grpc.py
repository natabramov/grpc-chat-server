# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import chat_pb2 as chat__pb2


class ChatServerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Channel_SendMessage = channel.unary_unary(
                '/grpc.ChatServer/Channel_SendMessage',
                request_serializer=chat__pb2.ChannelSendMessageRequest.SerializeToString,
                response_deserializer=chat__pb2.GenericResponse.FromString,
                )
        self.Channel_GetMessages = channel.unary_unary(
                '/grpc.ChatServer/Channel_GetMessages',
                request_serializer=chat__pb2.ChannelGetMessagesRequest.SerializeToString,
                response_deserializer=chat__pb2.ChannelGetMessagesResponse.FromString,
                )
        self.Channel_MemberUpdate = channel.unary_unary(
                '/grpc.ChatServer/Channel_MemberUpdate',
                request_serializer=chat__pb2.ChannelMemberUpdateRequest.SerializeToString,
                response_deserializer=chat__pb2.GenericResponse.FromString,
                )
        self.Channel_Create = channel.unary_unary(
                '/grpc.ChatServer/Channel_Create',
                request_serializer=chat__pb2.ChannelCreateRequest.SerializeToString,
                response_deserializer=chat__pb2.GenericResponse.FromString,
                )
        self.Channel_Delete = channel.unary_unary(
                '/grpc.ChatServer/Channel_Delete',
                request_serializer=chat__pb2.ChannelDeleteRequest.SerializeToString,
                response_deserializer=chat__pb2.GenericResponse.FromString,
                )
        self.Account_Create = channel.unary_unary(
                '/grpc.ChatServer/Account_Create',
                request_serializer=chat__pb2.AccountCreateRequest.SerializeToString,
                response_deserializer=chat__pb2.GenericResponse.FromString,
                )
        self.Account_Delete = channel.unary_unary(
                '/grpc.ChatServer/Account_Delete',
                request_serializer=chat__pb2.AccountCreateRequest.SerializeToString,
                response_deserializer=chat__pb2.GenericResponse.FromString,
                )
        self.Login = channel.unary_unary(
                '/grpc.ChatServer/Login',
                request_serializer=chat__pb2.LoginRequest.SerializeToString,
                response_deserializer=chat__pb2.GenericResponse.FromString,
                )
        self.Status = channel.unary_unary(
                '/grpc.ChatServer/Status',
                request_serializer=chat__pb2.Empty.SerializeToString,
                response_deserializer=chat__pb2.GenericResponse.FromString,
                )


class ChatServerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Channel_SendMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Channel_GetMessages(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Channel_MemberUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Channel_Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Channel_Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Account_Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Account_Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Login(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Status(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ChatServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Channel_SendMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.Channel_SendMessage,
                    request_deserializer=chat__pb2.ChannelSendMessageRequest.FromString,
                    response_serializer=chat__pb2.GenericResponse.SerializeToString,
            ),
            'Channel_GetMessages': grpc.unary_unary_rpc_method_handler(
                    servicer.Channel_GetMessages,
                    request_deserializer=chat__pb2.ChannelGetMessagesRequest.FromString,
                    response_serializer=chat__pb2.ChannelGetMessagesResponse.SerializeToString,
            ),
            'Channel_MemberUpdate': grpc.unary_unary_rpc_method_handler(
                    servicer.Channel_MemberUpdate,
                    request_deserializer=chat__pb2.ChannelMemberUpdateRequest.FromString,
                    response_serializer=chat__pb2.GenericResponse.SerializeToString,
            ),
            'Channel_Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Channel_Create,
                    request_deserializer=chat__pb2.ChannelCreateRequest.FromString,
                    response_serializer=chat__pb2.GenericResponse.SerializeToString,
            ),
            'Channel_Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Channel_Delete,
                    request_deserializer=chat__pb2.ChannelDeleteRequest.FromString,
                    response_serializer=chat__pb2.GenericResponse.SerializeToString,
            ),
            'Account_Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Account_Create,
                    request_deserializer=chat__pb2.AccountCreateRequest.FromString,
                    response_serializer=chat__pb2.GenericResponse.SerializeToString,
            ),
            'Account_Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Account_Delete,
                    request_deserializer=chat__pb2.AccountCreateRequest.FromString,
                    response_serializer=chat__pb2.GenericResponse.SerializeToString,
            ),
            'Login': grpc.unary_unary_rpc_method_handler(
                    servicer.Login,
                    request_deserializer=chat__pb2.LoginRequest.FromString,
                    response_serializer=chat__pb2.GenericResponse.SerializeToString,
            ),
            'Status': grpc.unary_unary_rpc_method_handler(
                    servicer.Status,
                    request_deserializer=chat__pb2.Empty.FromString,
                    response_serializer=chat__pb2.GenericResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'grpc.ChatServer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ChatServer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Channel_SendMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.ChatServer/Channel_SendMessage',
            chat__pb2.ChannelSendMessageRequest.SerializeToString,
            chat__pb2.GenericResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Channel_GetMessages(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.ChatServer/Channel_GetMessages',
            chat__pb2.ChannelGetMessagesRequest.SerializeToString,
            chat__pb2.ChannelGetMessagesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Channel_MemberUpdate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.ChatServer/Channel_MemberUpdate',
            chat__pb2.ChannelMemberUpdateRequest.SerializeToString,
            chat__pb2.GenericResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Channel_Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.ChatServer/Channel_Create',
            chat__pb2.ChannelCreateRequest.SerializeToString,
            chat__pb2.GenericResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Channel_Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.ChatServer/Channel_Delete',
            chat__pb2.ChannelDeleteRequest.SerializeToString,
            chat__pb2.GenericResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Account_Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.ChatServer/Account_Create',
            chat__pb2.AccountCreateRequest.SerializeToString,
            chat__pb2.GenericResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Account_Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.ChatServer/Account_Delete',
            chat__pb2.AccountCreateRequest.SerializeToString,
            chat__pb2.GenericResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Login(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.ChatServer/Login',
            chat__pb2.LoginRequest.SerializeToString,
            chat__pb2.GenericResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Status(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.ChatServer/Status',
            chat__pb2.Empty.SerializeToString,
            chat__pb2.GenericResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
