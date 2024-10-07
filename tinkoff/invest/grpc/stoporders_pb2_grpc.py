# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from tinkoff.invest.grpc import stoporders_pb2 as tinkoff_dot_invest_dot_grpc_dot_stoporders__pb2

GRPC_GENERATED_VERSION = '1.64.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in tinkoff/invest/grpc/stoporders_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class StopOrdersServiceStub(object):
    """Сервис предназначен для работы со стоп-заявками:</br> **1**.
    выставление;</br> **2**. отмена;</br> **3**. получение списка стоп-заявок.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PostStopOrder = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.StopOrdersService/PostStopOrder',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_stoporders__pb2.PostStopOrderRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_stoporders__pb2.PostStopOrderResponse.FromString,
                _registered_method=True)
        self.GetStopOrders = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.StopOrdersService/GetStopOrders',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_stoporders__pb2.GetStopOrdersRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_stoporders__pb2.GetStopOrdersResponse.FromString,
                _registered_method=True)
        self.CancelStopOrder = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.StopOrdersService/CancelStopOrder',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_stoporders__pb2.CancelStopOrderRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_stoporders__pb2.CancelStopOrderResponse.FromString,
                _registered_method=True)


class StopOrdersServiceServicer(object):
    """Сервис предназначен для работы со стоп-заявками:</br> **1**.
    выставление;</br> **2**. отмена;</br> **3**. получение списка стоп-заявок.
    """

    def PostStopOrder(self, request, context):
        """Метод выставления стоп-заявки.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStopOrders(self, request, context):
        """Метод получения списка активных стоп заявок по счёту.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CancelStopOrder(self, request, context):
        """Метод отмены стоп-заявки.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StopOrdersServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'PostStopOrder': grpc.unary_unary_rpc_method_handler(
                    servicer.PostStopOrder,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_stoporders__pb2.PostStopOrderRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_stoporders__pb2.PostStopOrderResponse.SerializeToString,
            ),
            'GetStopOrders': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStopOrders,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_stoporders__pb2.GetStopOrdersRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_stoporders__pb2.GetStopOrdersResponse.SerializeToString,
            ),
            'CancelStopOrder': grpc.unary_unary_rpc_method_handler(
                    servicer.CancelStopOrder,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_stoporders__pb2.CancelStopOrderRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_stoporders__pb2.CancelStopOrderResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'tinkoff.public.invest.api.contract.v1.StopOrdersService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('tinkoff.public.invest.api.contract.v1.StopOrdersService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class StopOrdersService(object):
    """Сервис предназначен для работы со стоп-заявками:</br> **1**.
    выставление;</br> **2**. отмена;</br> **3**. получение списка стоп-заявок.
    """

    @staticmethod
    def PostStopOrder(request,
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
            '/tinkoff.public.invest.api.contract.v1.StopOrdersService/PostStopOrder',
            tinkoff_dot_invest_dot_grpc_dot_stoporders__pb2.PostStopOrderRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_stoporders__pb2.PostStopOrderResponse.FromString,
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
    def GetStopOrders(request,
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
            '/tinkoff.public.invest.api.contract.v1.StopOrdersService/GetStopOrders',
            tinkoff_dot_invest_dot_grpc_dot_stoporders__pb2.GetStopOrdersRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_stoporders__pb2.GetStopOrdersResponse.FromString,
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
    def CancelStopOrder(request,
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
            '/tinkoff.public.invest.api.contract.v1.StopOrdersService/CancelStopOrder',
            tinkoff_dot_invest_dot_grpc_dot_stoporders__pb2.CancelStopOrderRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_stoporders__pb2.CancelStopOrderResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
