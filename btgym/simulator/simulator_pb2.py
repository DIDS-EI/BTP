# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: simulator.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'simulator.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fsimulator.proto\x12\tsimulator\"\x07\n\x05\x45mpty\"$\n\x0fLoadTaskRequest\x12\x11\n\ttask_name\x18\x01 \x01(\t\".\n\x17NavigateToObjectRequest\x12\x13\n\x0bobject_name\x18\x01 \x01(\t\"\'\n\x11SceneNameResponse\x12\x12\n\nscene_name\x18\x01 \x01(\t\"$\n\x10RobotPosResponse\x12\x10\n\x08position\x18\x01 \x03(\x02\"\\\n\rImageResponse\x12\x0b\n\x03rgb\x18\x01 \x01(\x0c\x12\r\n\x05\x64\x65pth\x18\x02 \x01(\x0c\x12\x0e\n\x06height\x18\x03 \x01(\x05\x12\r\n\x05width\x18\x04 \x01(\x05\x12\x10\n\x08\x63hannels\x18\x05 \x01(\x05\"3\n\x1bGetRobotJointStatesResponse\x12\x14\n\x0cjoint_states\x18\x01 \x03(\x02\"2\n\x1aSetRobotJointStatesRequest\x12\x14\n\x0cjoint_states\x18\x01 \x03(\x02\"#\n\x0f\x45\x45\x46PoseResponse\x12\x10\n\x08\x65\x65\x66_pose\x18\x01 \x03(\x02\"4\n\x17RelativeEEFPoseResponse\x12\x19\n\x11relative_eef_pose\x18\x01 \x03(\x02\"+\n\x13TaskObjectsResponse\x12\x14\n\x0cobject_names\x18\x01 \x03(\t\")\n\x12GraspObjectRequest\x12\x13\n\x0bobject_name\x18\x01 \x01(\t\"2\n\x10ReachPoseRequest\x12\x0c\n\x04pose\x18\x01 \x03(\x02\x12\x10\n\x08is_local\x18\x02 \x01(\x08\"-\n\x16SaveCameraImageRequest\x12\x13\n\x0boutput_path\x18\x01 \x01(\t2\x87\x08\n\x10SimulatorService\x12:\n\x08LoadTask\x12\x1a.simulator.LoadTaskRequest\x1a\x10.simulator.Empty\"\x00\x12<\n\x14InitActionPrimitives\x12\x10.simulator.Empty\x1a\x10.simulator.Empty\"\x00\x12J\n\x10NavigateToObject\x12\".simulator.NavigateToObjectRequest\x1a\x10.simulator.Empty\"\x00\x12@\n\x0cGetSceneName\x12\x10.simulator.Empty\x1a\x1c.simulator.SceneNameResponse\"\x00\x12>\n\x0bGetRobotPos\x12\x10.simulator.Empty\x1a\x1b.simulator.RobotPosResponse\"\x00\x12,\n\x04Step\x12\x10.simulator.Empty\x1a\x10.simulator.Empty\"\x00\x12\x37\n\x07GetRGBD\x12\x10.simulator.Empty\x1a\x18.simulator.ImageResponse\"\x00\x12Q\n\x13GetRobotJointStates\x12\x10.simulator.Empty\x1a&.simulator.GetRobotJointStatesResponse\"\x00\x12P\n\x13SetRobotJointStates\x12%.simulator.SetRobotJointStatesRequest\x1a\x10.simulator.Empty\"\x00\x12\x41\n\x0fGetRobotEEFPose\x12\x10.simulator.Empty\x1a\x1a.simulator.EEFPoseResponse\"\x00\x12L\n\x12GetRelativeEEFPose\x12\x10.simulator.Empty\x1a\".simulator.RelativeEEFPoseResponse\"\x00\x12\x44\n\x0eGetTaskObjects\x12\x10.simulator.Empty\x1a\x1e.simulator.TaskObjectsResponse\"\x00\x12@\n\x0bGraspObject\x12\x1d.simulator.GraspObjectRequest\x1a\x10.simulator.Empty\"\x00\x12<\n\tReachPose\x12\x1b.simulator.ReachPoseRequest\x1a\x10.simulator.Empty\"\x00\x12H\n\x0fSaveCameraImage\x12!.simulator.SaveCameraImageRequest\x1a\x10.simulator.Empty\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'simulator_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_EMPTY']._serialized_start=30
  _globals['_EMPTY']._serialized_end=37
  _globals['_LOADTASKREQUEST']._serialized_start=39
  _globals['_LOADTASKREQUEST']._serialized_end=75
  _globals['_NAVIGATETOOBJECTREQUEST']._serialized_start=77
  _globals['_NAVIGATETOOBJECTREQUEST']._serialized_end=123
  _globals['_SCENENAMERESPONSE']._serialized_start=125
  _globals['_SCENENAMERESPONSE']._serialized_end=164
  _globals['_ROBOTPOSRESPONSE']._serialized_start=166
  _globals['_ROBOTPOSRESPONSE']._serialized_end=202
  _globals['_IMAGERESPONSE']._serialized_start=204
  _globals['_IMAGERESPONSE']._serialized_end=296
  _globals['_GETROBOTJOINTSTATESRESPONSE']._serialized_start=298
  _globals['_GETROBOTJOINTSTATESRESPONSE']._serialized_end=349
  _globals['_SETROBOTJOINTSTATESREQUEST']._serialized_start=351
  _globals['_SETROBOTJOINTSTATESREQUEST']._serialized_end=401
  _globals['_EEFPOSERESPONSE']._serialized_start=403
  _globals['_EEFPOSERESPONSE']._serialized_end=438
  _globals['_RELATIVEEEFPOSERESPONSE']._serialized_start=440
  _globals['_RELATIVEEEFPOSERESPONSE']._serialized_end=492
  _globals['_TASKOBJECTSRESPONSE']._serialized_start=494
  _globals['_TASKOBJECTSRESPONSE']._serialized_end=537
  _globals['_GRASPOBJECTREQUEST']._serialized_start=539
  _globals['_GRASPOBJECTREQUEST']._serialized_end=580
  _globals['_REACHPOSEREQUEST']._serialized_start=582
  _globals['_REACHPOSEREQUEST']._serialized_end=632
  _globals['_SAVECAMERAIMAGEREQUEST']._serialized_start=634
  _globals['_SAVECAMERAIMAGEREQUEST']._serialized_end=679
  _globals['_SIMULATORSERVICE']._serialized_start=682
  _globals['_SIMULATORSERVICE']._serialized_end=1713
# @@protoc_insertion_point(module_scope)
