# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chat.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nchat.proto\x12\x04grpc\"\'\n\x08\x41uthUser\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05token\x18\x02 \x01(\t\"U\n\x0b\x43hatMessage\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x11\n\x04\x66ont\x18\x02 \x01(\rH\x00\x88\x01\x01\x12\x12\n\x05style\x18\x03 \x01(\rH\x01\x88\x01\x01\x42\x07\n\x05_fontB\x08\n\x06_style\"\x1b\n\x0cImageMessage\x12\x0b\n\x03url\x18\x01 \x01(\t\"\x84\x01\n\x0e\x43hannelMessage\x12\x0c\n\x04user\x18\x01 \x01(\t\x12!\n\x04\x63hat\x18\x02 \x01(\x0b\x32\x11.grpc.ChatMessageH\x00\x12#\n\x05image\x18\x03 \x01(\x0b\x32\x12.grpc.ImageMessageH\x00\x12\x11\n\ttimestamp\x18\x04 \x01(\x04\x42\t\n\x07message\"a\n\x07\x43hannel\x12\r\n\x05topic\x18\x01 \x01(\t\x12\r\n\x05users\x18\x02 \x03(\t\x12&\n\x08messages\x18\x03 \x03(\x0b\x32\x14.grpc.ChannelMessage\x12\x10\n\x08password\x18\x04 \x01(\t\"V\n\x0fGenericResponse\x12\x12\n\nsuccessful\x18\x01 \x01(\x08\x12\x12\n\x05\x65rror\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x11\n\ttimestamp\x18\x03 \x01(\x04\x42\x08\n\x06_error\"\xb0\x01\n\x19\x43hannelSendMessageRequest\x12\x1c\n\x04user\x18\x01 \x01(\x0b\x32\x0e.grpc.AuthUser\x12\x0f\n\x07\x63hannel\x18\x02 \x01(\t\x12!\n\x04\x63hat\x18\x03 \x01(\x0b\x32\x11.grpc.ChatMessageH\x00\x12#\n\x05image\x18\x04 \x01(\x0b\x32\x12.grpc.ImageMessageH\x00\x12\x11\n\ttimestamp\x18\x05 \x01(\x04\x42\t\n\x07message\"Y\n\x19\x43hannelGetMessagesRequest\x12\x1c\n\x04user\x18\x01 \x01(\x0b\x32\x0e.grpc.AuthUser\x12\x0f\n\x07\x63hannel\x18\x02 \x01(\t\x12\r\n\x05since\x18\x03 \x01(\x04\"k\n\x1a\x43hannelGetMessagesResponse\x12\x12\n\nsuccessful\x18\x01 \x01(\x08\x12&\n\x08messages\x18\x02 \x03(\x0b\x32\x14.grpc.ChannelMessage\x12\x11\n\ttimestamp\x18\x03 \x01(\x04\"\xe0\x01\n\x1a\x43hannelMemberUpdateRequest\x12\x1c\n\x04user\x18\x01 \x01(\x0b\x32\x0e.grpc.AuthUser\x12\x0f\n\x07\x63hannel\x18\x02 \x01(\t\x12\x15\n\x08password\x18\x03 \x01(\tH\x00\x88\x01\x01\x12\x39\n\x04type\x18\x04 \x01(\x0e\x32+.grpc.ChannelMemberUpdateRequest.UpdateType\x12\x11\n\ttimestamp\x18\x05 \x01(\x04\"!\n\nUpdateType\x12\x08\n\x04Join\x10\x00\x12\t\n\x05Leave\x10\x01\x42\x0b\n\t_password2\x8c\x02\n\nChatServer\x12O\n\x13\x43hannel_SendMessage\x12\x1f.grpc.ChannelSendMessageRequest\x1a\x15.grpc.GenericResponse\"\x00\x12Z\n\x13\x43hannel_GetMessages\x12\x1f.grpc.ChannelGetMessagesRequest\x1a .grpc.ChannelGetMessagesResponse\"\x00\x12Q\n\x14\x43hannel_MemberUpdate\x12 .grpc.ChannelMemberUpdateRequest\x1a\x15.grpc.GenericResponse\"\x00\x62\x06proto3')



_AUTHUSER = DESCRIPTOR.message_types_by_name['AuthUser']
_CHATMESSAGE = DESCRIPTOR.message_types_by_name['ChatMessage']
_IMAGEMESSAGE = DESCRIPTOR.message_types_by_name['ImageMessage']
_CHANNELMESSAGE = DESCRIPTOR.message_types_by_name['ChannelMessage']
_CHANNEL = DESCRIPTOR.message_types_by_name['Channel']
_GENERICRESPONSE = DESCRIPTOR.message_types_by_name['GenericResponse']
_CHANNELSENDMESSAGEREQUEST = DESCRIPTOR.message_types_by_name['ChannelSendMessageRequest']
_CHANNELGETMESSAGESREQUEST = DESCRIPTOR.message_types_by_name['ChannelGetMessagesRequest']
_CHANNELGETMESSAGESRESPONSE = DESCRIPTOR.message_types_by_name['ChannelGetMessagesResponse']
_CHANNELMEMBERUPDATEREQUEST = DESCRIPTOR.message_types_by_name['ChannelMemberUpdateRequest']
_CHANNELMEMBERUPDATEREQUEST_UPDATETYPE = _CHANNELMEMBERUPDATEREQUEST.enum_types_by_name['UpdateType']
AuthUser = _reflection.GeneratedProtocolMessageType('AuthUser', (_message.Message,), {
  'DESCRIPTOR' : _AUTHUSER,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:grpc.AuthUser)
  })
_sym_db.RegisterMessage(AuthUser)

ChatMessage = _reflection.GeneratedProtocolMessageType('ChatMessage', (_message.Message,), {
  'DESCRIPTOR' : _CHATMESSAGE,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:grpc.ChatMessage)
  })
_sym_db.RegisterMessage(ChatMessage)

ImageMessage = _reflection.GeneratedProtocolMessageType('ImageMessage', (_message.Message,), {
  'DESCRIPTOR' : _IMAGEMESSAGE,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:grpc.ImageMessage)
  })
_sym_db.RegisterMessage(ImageMessage)

ChannelMessage = _reflection.GeneratedProtocolMessageType('ChannelMessage', (_message.Message,), {
  'DESCRIPTOR' : _CHANNELMESSAGE,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:grpc.ChannelMessage)
  })
_sym_db.RegisterMessage(ChannelMessage)

Channel = _reflection.GeneratedProtocolMessageType('Channel', (_message.Message,), {
  'DESCRIPTOR' : _CHANNEL,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:grpc.Channel)
  })
_sym_db.RegisterMessage(Channel)

GenericResponse = _reflection.GeneratedProtocolMessageType('GenericResponse', (_message.Message,), {
  'DESCRIPTOR' : _GENERICRESPONSE,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:grpc.GenericResponse)
  })
_sym_db.RegisterMessage(GenericResponse)

ChannelSendMessageRequest = _reflection.GeneratedProtocolMessageType('ChannelSendMessageRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHANNELSENDMESSAGEREQUEST,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:grpc.ChannelSendMessageRequest)
  })
_sym_db.RegisterMessage(ChannelSendMessageRequest)

ChannelGetMessagesRequest = _reflection.GeneratedProtocolMessageType('ChannelGetMessagesRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHANNELGETMESSAGESREQUEST,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:grpc.ChannelGetMessagesRequest)
  })
_sym_db.RegisterMessage(ChannelGetMessagesRequest)

ChannelGetMessagesResponse = _reflection.GeneratedProtocolMessageType('ChannelGetMessagesResponse', (_message.Message,), {
  'DESCRIPTOR' : _CHANNELGETMESSAGESRESPONSE,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:grpc.ChannelGetMessagesResponse)
  })
_sym_db.RegisterMessage(ChannelGetMessagesResponse)

ChannelMemberUpdateRequest = _reflection.GeneratedProtocolMessageType('ChannelMemberUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHANNELMEMBERUPDATEREQUEST,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:grpc.ChannelMemberUpdateRequest)
  })
_sym_db.RegisterMessage(ChannelMemberUpdateRequest)

_CHATSERVER = DESCRIPTOR.services_by_name['ChatServer']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _AUTHUSER._serialized_start=20
  _AUTHUSER._serialized_end=59
  _CHATMESSAGE._serialized_start=61
  _CHATMESSAGE._serialized_end=146
  _IMAGEMESSAGE._serialized_start=148
  _IMAGEMESSAGE._serialized_end=175
  _CHANNELMESSAGE._serialized_start=178
  _CHANNELMESSAGE._serialized_end=310
  _CHANNEL._serialized_start=312
  _CHANNEL._serialized_end=409
  _GENERICRESPONSE._serialized_start=411
  _GENERICRESPONSE._serialized_end=497
  _CHANNELSENDMESSAGEREQUEST._serialized_start=500
  _CHANNELSENDMESSAGEREQUEST._serialized_end=676
  _CHANNELGETMESSAGESREQUEST._serialized_start=678
  _CHANNELGETMESSAGESREQUEST._serialized_end=767
  _CHANNELGETMESSAGESRESPONSE._serialized_start=769
  _CHANNELGETMESSAGESRESPONSE._serialized_end=876
  _CHANNELMEMBERUPDATEREQUEST._serialized_start=879
  _CHANNELMEMBERUPDATEREQUEST._serialized_end=1103
  _CHANNELMEMBERUPDATEREQUEST_UPDATETYPE._serialized_start=1057
  _CHANNELMEMBERUPDATEREQUEST_UPDATETYPE._serialized_end=1090
  _CHATSERVER._serialized_start=1106
  _CHATSERVER._serialized_end=1374
# @@protoc_insertion_point(module_scope)
