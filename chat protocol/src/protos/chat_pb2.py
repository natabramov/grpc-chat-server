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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nchat.proto\x12\x04grpc\"T\n\x0b\x43hatRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x0f\n\x07\x63hannel\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t\x12\x11\n\ttimestamp\x18\x04 \x01(\x04\"2\n\tChatReply\x12\x12\n\nsuccessful\x18\x01 \x01(\x08\x12\x11\n\ttimestamp\x18\x02 \x01(\x04\x32>\n\nChatServer\x12\x30\n\x08SendChat\x12\x11.grpc.ChatRequest\x1a\x0f.grpc.ChatReply\"\x00\x62\x06proto3')



_CHATREQUEST = DESCRIPTOR.message_types_by_name['ChatRequest']
_CHATREPLY = DESCRIPTOR.message_types_by_name['ChatReply']
ChatRequest = _reflection.GeneratedProtocolMessageType('ChatRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHATREQUEST,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:grpc.ChatRequest)
  })
_sym_db.RegisterMessage(ChatRequest)

ChatReply = _reflection.GeneratedProtocolMessageType('ChatReply', (_message.Message,), {
  'DESCRIPTOR' : _CHATREPLY,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:grpc.ChatReply)
  })
_sym_db.RegisterMessage(ChatReply)

_CHATSERVER = DESCRIPTOR.services_by_name['ChatServer']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CHATREQUEST._serialized_start=20
  _CHATREQUEST._serialized_end=104
  _CHATREPLY._serialized_start=106
  _CHATREPLY._serialized_end=156
  _CHATSERVER._serialized_start=158
  _CHATSERVER._serialized_end=220
# @@protoc_insertion_point(module_scope)