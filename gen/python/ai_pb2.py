# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: ai.proto
# Protobuf Python Version: 6.31.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    31,
    0,
    '',
    'ai.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x08\x61i.proto\x12\x02\x61i\"\x1c\n\nReqRequest\x12\x0e\n\x06prompt\x18\x01 \x01(\t\"\x1c\n\x0bReqResponse\x12\r\n\x05\x63hunk\x18\x01 \x01(\t\"\x1d\n\x0bTestRequest\x12\x0e\n\x06prompt\x18\x01 \x01(\t\"\x1d\n\x0cTestResponse\x12\r\n\x05\x63hunk\x18\x01 \x01(\t2^\n\x02\x41i\x12-\n\x08Requests\x12\x0e.ai.ReqRequest\x1a\x0f.ai.ReqResponse0\x01\x12)\n\x04Test\x12\x0f.ai.TestRequest\x1a\x10.ai.TestResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ai_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_REQREQUEST']._serialized_start=16
  _globals['_REQREQUEST']._serialized_end=44
  _globals['_REQRESPONSE']._serialized_start=46
  _globals['_REQRESPONSE']._serialized_end=74
  _globals['_TESTREQUEST']._serialized_start=76
  _globals['_TESTREQUEST']._serialized_end=105
  _globals['_TESTRESPONSE']._serialized_start=107
  _globals['_TESTRESPONSE']._serialized_end=136
  _globals['_AI']._serialized_start=138
  _globals['_AI']._serialized_end=232
# @@protoc_insertion_point(module_scope)
