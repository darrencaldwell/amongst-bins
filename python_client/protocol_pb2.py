# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protocol.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protocol.proto',
  package='protocol',
  syntax='proto3',
  serialized_options=b'Z.github.com/CynicalCode21/amongst-bins/protocol',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0eprotocol.proto\x12\x08protocol\"\x1c\n\x08JoinGame\x12\x10\n\x08username\x18\x01 \x01(\t\"!\n\x0c\x45\x63hoJoinGame\x12\x11\n\tplayer_id\x18\x01 \x01(\x05\"9\n\x0ePlayerPosition\x12\x11\n\tplayer_id\x18\x01 \x01(\x03\x12\t\n\x01x\x18\x02 \x01(\x03\x12\t\n\x01y\x18\x03 \x01(\x03\">\n\x0e\x43lientMovement\x12,\n\nplayer_pos\x18\x01 \x01(\x0b\x32\x18.protocol.PlayerPosition\"D\n\x14ServerPositionUpdate\x12,\n\nplayer_pos\x18\x01 \x03(\x0b\x32\x18.protocol.PlayerPositionB0Z.github.com/CynicalCode21/amongst-bins/protocolb\x06proto3'
)




_JOINGAME = _descriptor.Descriptor(
  name='JoinGame',
  full_name='protocol.JoinGame',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='protocol.JoinGame.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=56,
)


_ECHOJOINGAME = _descriptor.Descriptor(
  name='EchoJoinGame',
  full_name='protocol.EchoJoinGame',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='player_id', full_name='protocol.EchoJoinGame.player_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=58,
  serialized_end=91,
)


_PLAYERPOSITION = _descriptor.Descriptor(
  name='PlayerPosition',
  full_name='protocol.PlayerPosition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='player_id', full_name='protocol.PlayerPosition.player_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='x', full_name='protocol.PlayerPosition.x', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='protocol.PlayerPosition.y', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=93,
  serialized_end=150,
)


_CLIENTMOVEMENT = _descriptor.Descriptor(
  name='ClientMovement',
  full_name='protocol.ClientMovement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='player_pos', full_name='protocol.ClientMovement.player_pos', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=152,
  serialized_end=214,
)


_SERVERPOSITIONUPDATE = _descriptor.Descriptor(
  name='ServerPositionUpdate',
  full_name='protocol.ServerPositionUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='player_pos', full_name='protocol.ServerPositionUpdate.player_pos', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=216,
  serialized_end=284,
)

_CLIENTMOVEMENT.fields_by_name['player_pos'].message_type = _PLAYERPOSITION
_SERVERPOSITIONUPDATE.fields_by_name['player_pos'].message_type = _PLAYERPOSITION
DESCRIPTOR.message_types_by_name['JoinGame'] = _JOINGAME
DESCRIPTOR.message_types_by_name['EchoJoinGame'] = _ECHOJOINGAME
DESCRIPTOR.message_types_by_name['PlayerPosition'] = _PLAYERPOSITION
DESCRIPTOR.message_types_by_name['ClientMovement'] = _CLIENTMOVEMENT
DESCRIPTOR.message_types_by_name['ServerPositionUpdate'] = _SERVERPOSITIONUPDATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

JoinGame = _reflection.GeneratedProtocolMessageType('JoinGame', (_message.Message,), {
  'DESCRIPTOR' : _JOINGAME,
  '__module__' : 'protocol_pb2'
  # @@protoc_insertion_point(class_scope:protocol.JoinGame)
  })
_sym_db.RegisterMessage(JoinGame)

EchoJoinGame = _reflection.GeneratedProtocolMessageType('EchoJoinGame', (_message.Message,), {
  'DESCRIPTOR' : _ECHOJOINGAME,
  '__module__' : 'protocol_pb2'
  # @@protoc_insertion_point(class_scope:protocol.EchoJoinGame)
  })
_sym_db.RegisterMessage(EchoJoinGame)

PlayerPosition = _reflection.GeneratedProtocolMessageType('PlayerPosition', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERPOSITION,
  '__module__' : 'protocol_pb2'
  # @@protoc_insertion_point(class_scope:protocol.PlayerPosition)
  })
_sym_db.RegisterMessage(PlayerPosition)

ClientMovement = _reflection.GeneratedProtocolMessageType('ClientMovement', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTMOVEMENT,
  '__module__' : 'protocol_pb2'
  # @@protoc_insertion_point(class_scope:protocol.ClientMovement)
  })
_sym_db.RegisterMessage(ClientMovement)

ServerPositionUpdate = _reflection.GeneratedProtocolMessageType('ServerPositionUpdate', (_message.Message,), {
  'DESCRIPTOR' : _SERVERPOSITIONUPDATE,
  '__module__' : 'protocol_pb2'
  # @@protoc_insertion_point(class_scope:protocol.ServerPositionUpdate)
  })
_sym_db.RegisterMessage(ServerPositionUpdate)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)