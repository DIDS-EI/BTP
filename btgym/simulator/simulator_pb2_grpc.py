# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import btgym.simulator.simulator_pb2 as simulator__pb2

GRPC_GENERATED_VERSION = '1.68.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in simulator_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class SimulatorServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.LoadTask = channel.unary_unary(
                '/simulator.SimulatorService/LoadTask',
                request_serializer=simulator__pb2.LoadTaskRequest.SerializeToString,
                response_deserializer=simulator__pb2.CommonResponse.FromString,
                _registered_method=True)
        self.InitActionPrimitives = channel.unary_unary(
                '/simulator.SimulatorService/InitActionPrimitives',
                request_serializer=simulator__pb2.Empty.SerializeToString,
                response_deserializer=simulator__pb2.CommonResponse.FromString,
                _registered_method=True)
        self.NavigateToObject = channel.unary_unary(
                '/simulator.SimulatorService/NavigateToObject',
                request_serializer=simulator__pb2.NavigateRequest.SerializeToString,
                response_deserializer=simulator__pb2.CommonResponse.FromString,
                _registered_method=True)
        self.GetSceneName = channel.unary_unary(
                '/simulator.SimulatorService/GetSceneName',
                request_serializer=simulator__pb2.Empty.SerializeToString,
                response_deserializer=simulator__pb2.SceneNameResponse.FromString,
                _registered_method=True)
        self.GetRobotPos = channel.unary_unary(
                '/simulator.SimulatorService/GetRobotPos',
                request_serializer=simulator__pb2.Empty.SerializeToString,
                response_deserializer=simulator__pb2.RobotPosResponse.FromString,
                _registered_method=True)
        self.Step = channel.unary_unary(
                '/simulator.SimulatorService/Step',
                request_serializer=simulator__pb2.Empty.SerializeToString,
                response_deserializer=simulator__pb2.CommonResponse.FromString,
                _registered_method=True)
        self.GetRGBD = channel.unary_unary(
                '/simulator.SimulatorService/GetRGBD',
                request_serializer=simulator__pb2.Empty.SerializeToString,
                response_deserializer=simulator__pb2.ImageResponse.FromString,
                _registered_method=True)


class SimulatorServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def LoadTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InitActionPrimitives(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NavigateToObject(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSceneName(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRobotPos(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Step(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRGBD(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SimulatorServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'LoadTask': grpc.unary_unary_rpc_method_handler(
                    servicer.LoadTask,
                    request_deserializer=simulator__pb2.LoadTaskRequest.FromString,
                    response_serializer=simulator__pb2.CommonResponse.SerializeToString,
            ),
            'InitActionPrimitives': grpc.unary_unary_rpc_method_handler(
                    servicer.InitActionPrimitives,
                    request_deserializer=simulator__pb2.Empty.FromString,
                    response_serializer=simulator__pb2.CommonResponse.SerializeToString,
            ),
            'NavigateToObject': grpc.unary_unary_rpc_method_handler(
                    servicer.NavigateToObject,
                    request_deserializer=simulator__pb2.NavigateRequest.FromString,
                    response_serializer=simulator__pb2.CommonResponse.SerializeToString,
            ),
            'GetSceneName': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSceneName,
                    request_deserializer=simulator__pb2.Empty.FromString,
                    response_serializer=simulator__pb2.SceneNameResponse.SerializeToString,
            ),
            'GetRobotPos': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRobotPos,
                    request_deserializer=simulator__pb2.Empty.FromString,
                    response_serializer=simulator__pb2.RobotPosResponse.SerializeToString,
            ),
            'Step': grpc.unary_unary_rpc_method_handler(
                    servicer.Step,
                    request_deserializer=simulator__pb2.Empty.FromString,
                    response_serializer=simulator__pb2.CommonResponse.SerializeToString,
            ),
            'GetRGBD': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRGBD,
                    request_deserializer=simulator__pb2.Empty.FromString,
                    response_serializer=simulator__pb2.ImageResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'simulator.SimulatorService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('simulator.SimulatorService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class SimulatorService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def LoadTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/simulator.SimulatorService/LoadTask',
            simulator__pb2.LoadTaskRequest.SerializeToString,
            simulator__pb2.CommonResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def InitActionPrimitives(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/simulator.SimulatorService/InitActionPrimitives',
            simulator__pb2.Empty.SerializeToString,
            simulator__pb2.CommonResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def NavigateToObject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/simulator.SimulatorService/NavigateToObject',
            simulator__pb2.NavigateRequest.SerializeToString,
            simulator__pb2.CommonResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetSceneName(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/simulator.SimulatorService/GetSceneName',
            simulator__pb2.Empty.SerializeToString,
            simulator__pb2.SceneNameResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetRobotPos(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/simulator.SimulatorService/GetRobotPos',
            simulator__pb2.Empty.SerializeToString,
            simulator__pb2.RobotPosResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Step(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/simulator.SimulatorService/Step',
            simulator__pb2.Empty.SerializeToString,
            simulator__pb2.CommonResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetRGBD(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/simulator.SimulatorService/GetRGBD',
            simulator__pb2.Empty.SerializeToString,
            simulator__pb2.ImageResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
