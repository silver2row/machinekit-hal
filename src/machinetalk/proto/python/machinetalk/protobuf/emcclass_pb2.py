# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: machinetalk/protobuf/emcclass.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from machinetalk.protobuf import nanopb_pb2 as machinetalk_dot_protobuf_dot_nanopb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='machinetalk/protobuf/emcclass.proto',
  package='machinetalk',
  syntax='proto2',
  serialized_pb=_b('\n#machinetalk/protobuf/emcclass.proto\x12\x0bmachinetalk\x1a!machinetalk/protobuf/nanopb.proto\"6\n\x0bPmCartesian\x12\t\n\x01x\x18\n \x01(\x01\x12\t\n\x01y\x18\x14 \x01(\x01\x12\t\n\x01z\x18\x1e \x01(\x01:\x06\x92?\x03H\xac\x02\"{\n\x07\x45mcPose\x12&\n\x04tran\x18\n \x02(\x0b\x32\x18.machinetalk.PmCartesian\x12\t\n\x01\x61\x18\x14 \x01(\x01\x12\t\n\x01\x62\x18\x1e \x01(\x01\x12\t\n\x01\x63\x18( \x01(\x01\x12\t\n\x01u\x18\x32 \x01(\x01\x12\t\n\x01v\x18< \x01(\x01\x12\t\n\x01w\x18\x46 \x01(\x01:\x06\x92?\x03H\xad\x02')
  ,
  dependencies=[machinetalk_dot_protobuf_dot_nanopb__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PMCARTESIAN = _descriptor.Descriptor(
  name='PmCartesian',
  full_name='machinetalk.PmCartesian',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='machinetalk.PmCartesian.x', index=0,
      number=10, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='machinetalk.PmCartesian.y', index=1,
      number=20, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='z', full_name='machinetalk.PmCartesian.z', index=2,
      number=30, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\222?\003H\254\002')),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=87,
  serialized_end=141,
)


_EMCPOSE = _descriptor.Descriptor(
  name='EmcPose',
  full_name='machinetalk.EmcPose',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tran', full_name='machinetalk.EmcPose.tran', index=0,
      number=10, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='a', full_name='machinetalk.EmcPose.a', index=1,
      number=20, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='b', full_name='machinetalk.EmcPose.b', index=2,
      number=30, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='c', full_name='machinetalk.EmcPose.c', index=3,
      number=40, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='u', full_name='machinetalk.EmcPose.u', index=4,
      number=50, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='v', full_name='machinetalk.EmcPose.v', index=5,
      number=60, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='w', full_name='machinetalk.EmcPose.w', index=6,
      number=70, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\222?\003H\255\002')),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=143,
  serialized_end=266,
)

_EMCPOSE.fields_by_name['tran'].message_type = _PMCARTESIAN
DESCRIPTOR.message_types_by_name['PmCartesian'] = _PMCARTESIAN
DESCRIPTOR.message_types_by_name['EmcPose'] = _EMCPOSE

PmCartesian = _reflection.GeneratedProtocolMessageType('PmCartesian', (_message.Message,), dict(
  DESCRIPTOR = _PMCARTESIAN,
  __module__ = 'machinetalk.protobuf.emcclass_pb2'
  # @@protoc_insertion_point(class_scope:machinetalk.PmCartesian)
  ))
_sym_db.RegisterMessage(PmCartesian)

EmcPose = _reflection.GeneratedProtocolMessageType('EmcPose', (_message.Message,), dict(
  DESCRIPTOR = _EMCPOSE,
  __module__ = 'machinetalk.protobuf.emcclass_pb2'
  # @@protoc_insertion_point(class_scope:machinetalk.EmcPose)
  ))
_sym_db.RegisterMessage(EmcPose)


_PMCARTESIAN.has_options = True
_PMCARTESIAN._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\222?\003H\254\002'))
_EMCPOSE.has_options = True
_EMCPOSE._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\222?\003H\255\002'))
# @@protoc_insertion_point(module_scope)
