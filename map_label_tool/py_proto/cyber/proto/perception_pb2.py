# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cyber/proto/perception.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='cyber/proto/perception.proto',
  package='apollo.cyber.proto',
  syntax='proto2',
  serialized_pb=_b('\n\x1c\x63yber/proto/perception.proto\x12\x12\x61pollo.cyber.proto\"\x80\x01\n\nPerception\x12\x35\n\x06header\x18\x01 \x01(\x0b\x32%.apollo.cyber.proto.Perception.Header\x12\x0e\n\x06msg_id\x18\x02 \x01(\x04\x12\x0e\n\x06result\x18\x03 \x01(\x01\x1a\x1b\n\x06Header\x12\x11\n\ttimestamp\x18\x01 \x01(\x04')
)




_PERCEPTION_HEADER = _descriptor.Descriptor(
  name='Header',
  full_name='apollo.cyber.proto.Perception.Header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='apollo.cyber.proto.Perception.Header.timestamp', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=154,
  serialized_end=181,
)

_PERCEPTION = _descriptor.Descriptor(
  name='Perception',
  full_name='apollo.cyber.proto.Perception',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='apollo.cyber.proto.Perception.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='msg_id', full_name='apollo.cyber.proto.Perception.msg_id', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result', full_name='apollo.cyber.proto.Perception.result', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_PERCEPTION_HEADER, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=53,
  serialized_end=181,
)

_PERCEPTION_HEADER.containing_type = _PERCEPTION
_PERCEPTION.fields_by_name['header'].message_type = _PERCEPTION_HEADER
DESCRIPTOR.message_types_by_name['Perception'] = _PERCEPTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Perception = _reflection.GeneratedProtocolMessageType('Perception', (_message.Message,), dict(

  Header = _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), dict(
    DESCRIPTOR = _PERCEPTION_HEADER,
    __module__ = 'cyber.proto.perception_pb2'
    # @@protoc_insertion_point(class_scope:apollo.cyber.proto.Perception.Header)
    ))
  ,
  DESCRIPTOR = _PERCEPTION,
  __module__ = 'cyber.proto.perception_pb2'
  # @@protoc_insertion_point(class_scope:apollo.cyber.proto.Perception)
  ))
_sym_db.RegisterMessage(Perception)
_sym_db.RegisterMessage(Perception.Header)


# @@protoc_insertion_point(module_scope)
