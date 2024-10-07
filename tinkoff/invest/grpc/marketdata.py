from base_service import BaseService
from dataclasses import dataclass
from datetime import datetime
from enum import IntEnum
from src.convertion import dataclass_to_protobuf
from src.convertion import protobuf_to_dataclass
from tinkoff.invest.grpc.common import Quotation
from tinkoff.invest.grpc.common import SecurityTradingStatus
from typing import Iterable
from typing import List
from typing import Optional


class MarketDataService(BaseService):
    """//Сервис получения биржевой информации:</br> **1**. свечи;</br> **2**. стаканы;</br> **3**. торговые статусы;</br> **4**. лента сделок."""
    _protobuf = marketdata_pb2
    _protobuf_grpc = marketdata_pb2_grpc
    _protobuf_stub = _protobuf_grpc.MarketDataServiceStub

    def GetCandles(self, request: 'GetCandlesRequest') ->'GetCandlesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetAccountsRequest())
        response, call = self._stub.GetAccounts.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, GetAccountsResponse)

    def GetLastPrices(self, request: 'GetLastPricesRequest'
        ) ->'GetLastPricesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetAccountsRequest())
        response, call = self._stub.GetAccounts.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, GetAccountsResponse)

    def GetOrderBook(self, request: 'GetOrderBookRequest'
        ) ->'GetOrderBookResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetAccountsRequest())
        response, call = self._stub.GetAccounts.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, GetAccountsResponse)

    def GetTradingStatus(self, request: 'GetTradingStatusRequest'
        ) ->'GetTradingStatusResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetAccountsRequest())
        response, call = self._stub.GetAccounts.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, GetAccountsResponse)

    def GetTradingStatuses(self, request: 'GetTradingStatusesRequest'
        ) ->'GetTradingStatusesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetAccountsRequest())
        response, call = self._stub.GetAccounts.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, GetAccountsResponse)

    def GetLastTrades(self, request: 'GetLastTradesRequest'
        ) ->'GetLastTradesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetAccountsRequest())
        response, call = self._stub.GetAccounts.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, GetAccountsResponse)

    def GetClosePrices(self, request: 'GetClosePricesRequest'
        ) ->'GetClosePricesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetAccountsRequest())
        response, call = self._stub.GetAccounts.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, GetAccountsResponse)

    def GetTechAnalysis(self, request: 'GetTechAnalysisRequest'
        ) ->'GetTechAnalysisResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetAccountsRequest())
        response, call = self._stub.GetAccounts.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, GetAccountsResponse)


class MarketDataStreamService(BaseService):
    """//Bi-directional стрим предоставления биржевой информации."""
    _protobuf = marketdata_pb2
    _protobuf_grpc = marketdata_pb2_grpc
    _protobuf_stub = _protobuf_grpc.MarketDataStreamServiceStub

    def MarketDataStream(self, requests: Iterable['MarketDataRequest']
        ) ->Iterable['MarketDataResponse']:
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetAccountsRequest())
        response, call = self._stub.GetAccounts.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, GetAccountsResponse)

    def MarketDataServerSideStream(self, request:
        'MarketDataServerSideStreamRequest') ->Iterable['MarketDataResponse']:
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetAccountsRequest())
        response, call = self._stub.GetAccounts.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, GetAccountsResponse)


@dataclass
class MarketDataRequest:
    pass


@dataclass
class MarketDataServerSideStreamRequest:
    subscribe_candles_request: 'SubscribeCandlesRequest'
    subscribe_order_book_request: 'SubscribeOrderBookRequest'
    subscribe_trades_request: 'SubscribeTradesRequest'
    subscribe_info_request: 'SubscribeInfoRequest'
    subscribe_last_price_request: 'SubscribeLastPriceRequest'


@dataclass
class MarketDataResponse:
    pass


@dataclass
class SubscribeCandlesRequest:
    subscription_action: 'SubscriptionAction'
    instruments: List['CandleInstrument']
    waiting_close: bool


class SubscriptionAction(IntEnum):
    SUBSCRIPTION_ACTION_UNSPECIFIED = 0
    SUBSCRIPTION_ACTION_SUBSCRIBE = 1
    SUBSCRIPTION_ACTION_UNSUBSCRIBE = 2


class SubscriptionInterval(IntEnum):
    SUBSCRIPTION_INTERVAL_UNSPECIFIED = 0
    SUBSCRIPTION_INTERVAL_ONE_MINUTE = 1
    SUBSCRIPTION_INTERVAL_FIVE_MINUTES = 2
    SUBSCRIPTION_INTERVAL_FIFTEEN_MINUTES = 3
    SUBSCRIPTION_INTERVAL_ONE_HOUR = 4
    SUBSCRIPTION_INTERVAL_ONE_DAY = 5
    SUBSCRIPTION_INTERVAL_2_MIN = 6
    SUBSCRIPTION_INTERVAL_3_MIN = 7
    SUBSCRIPTION_INTERVAL_10_MIN = 8
    SUBSCRIPTION_INTERVAL_30_MIN = 9
    SUBSCRIPTION_INTERVAL_2_HOUR = 10
    SUBSCRIPTION_INTERVAL_4_HOUR = 11
    SUBSCRIPTION_INTERVAL_WEEK = 12
    SUBSCRIPTION_INTERVAL_MONTH = 13


@dataclass
class CandleInstrument:
    figi: str
    interval: 'SubscriptionInterval'
    instrument_id: str


@dataclass
class SubscribeCandlesResponse:
    tracking_id: str
    candles_subscriptions: List['CandleSubscription']


@dataclass
class CandleSubscription:
    figi: str
    interval: 'SubscriptionInterval'
    subscription_status: 'SubscriptionStatus'
    instrument_uid: str
    waiting_close: bool
    stream_id: str
    subscription_id: str


class SubscriptionStatus(IntEnum):
    SUBSCRIPTION_STATUS_UNSPECIFIED = 0
    SUBSCRIPTION_STATUS_SUCCESS = 1
    SUBSCRIPTION_STATUS_INSTRUMENT_NOT_FOUND = 2
    SUBSCRIPTION_STATUS_SUBSCRIPTION_ACTION_IS_INVALID = 3
    SUBSCRIPTION_STATUS_DEPTH_IS_INVALID = 4
    SUBSCRIPTION_STATUS_INTERVAL_IS_INVALID = 5
    SUBSCRIPTION_STATUS_LIMIT_IS_EXCEEDED = 6
    SUBSCRIPTION_STATUS_INTERNAL_ERROR = 7
    SUBSCRIPTION_STATUS_TOO_MANY_REQUESTS = 8
    SUBSCRIPTION_STATUS_SUBSCRIPTION_NOT_FOUND = 9


@dataclass
class SubscribeOrderBookRequest:
    subscription_action: 'SubscriptionAction'
    instruments: List['OrderBookInstrument']


@dataclass
class OrderBookInstrument:
    figi: str
    depth: int
    instrument_id: str
    order_book_type: 'OrderBookType'


@dataclass
class SubscribeOrderBookResponse:
    tracking_id: str
    order_book_subscriptions: List['OrderBookSubscription']


@dataclass
class OrderBookSubscription:
    figi: str
    depth: int
    subscription_status: 'SubscriptionStatus'
    instrument_uid: str
    stream_id: str
    subscription_id: str
    order_book_type: 'OrderBookType'


class TradeSourceType(IntEnum):
    TRADE_SOURCE_UNSPECIFIED = 0
    TRADE_SOURCE_EXCHANGE = 1
    TRADE_SOURCE_DEALER = 2
    TRADE_SOURCE_ALL = 3


@dataclass
class SubscribeTradesRequest:
    subscription_action: 'SubscriptionAction'
    instruments: List['TradeInstrument']
    trade_type: 'TradeSourceType'


@dataclass
class TradeInstrument:
    figi: str
    instrument_id: str


@dataclass
class SubscribeTradesResponse:
    tracking_id: str
    trade_subscriptions: List['TradeSubscription']
    trade_type: 'TradeSourceType'


@dataclass
class TradeSubscription:
    figi: str
    subscription_status: 'SubscriptionStatus'
    instrument_uid: str
    stream_id: str
    subscription_id: str


@dataclass
class SubscribeInfoRequest:
    subscription_action: 'SubscriptionAction'
    instruments: List['InfoInstrument']


@dataclass
class InfoInstrument:
    figi: str
    instrument_id: str


@dataclass
class SubscribeInfoResponse:
    tracking_id: str
    info_subscriptions: List['InfoSubscription']


@dataclass
class InfoSubscription:
    figi: str
    subscription_status: 'SubscriptionStatus'
    instrument_uid: str
    stream_id: str
    subscription_id: str


@dataclass
class SubscribeLastPriceRequest:
    subscription_action: 'SubscriptionAction'
    instruments: List['LastPriceInstrument']


@dataclass
class LastPriceInstrument:
    figi: str
    instrument_id: str


@dataclass
class SubscribeLastPriceResponse:
    tracking_id: str
    last_price_subscriptions: List['LastPriceSubscription']


@dataclass
class LastPriceSubscription:
    figi: str
    subscription_status: 'SubscriptionStatus'
    instrument_uid: str
    stream_id: str
    subscription_id: str


@dataclass
class Candle:
    figi: str
    interval: 'SubscriptionInterval'
    open: 'Quotation'
    high: 'Quotation'
    low: 'Quotation'
    close: 'Quotation'
    volume: int
    time: datetime
    last_trade_ts: datetime
    instrument_uid: str


@dataclass
class OrderBook:
    figi: str
    depth: int
    is_consistent: bool
    bids: List['Order']
    asks: List['Order']
    time: datetime
    limit_up: 'Quotation'
    limit_down: 'Quotation'
    instrument_uid: str
    order_book_type: 'OrderBookType'


@dataclass
class Order:
    price: 'Quotation'
    quantity: int


@dataclass
class Trade:
    figi: str
    direction: 'TradeDirection'
    price: 'Quotation'
    quantity: int
    time: datetime
    instrument_uid: str
    tradeSource: 'TradeSourceType'


class TradeDirection(IntEnum):
    TRADE_DIRECTION_UNSPECIFIED = 0
    TRADE_DIRECTION_BUY = 1
    TRADE_DIRECTION_SELL = 2


@dataclass
class TradingStatus:
    figi: str
    trading_status: 'SecurityTradingStatus'
    time: datetime
    limit_order_available_flag: bool
    market_order_available_flag: bool
    instrument_uid: str


@dataclass
class GetCandlesRequest:
    from_: datetime
    to: datetime
    interval: 'CandleInterval'
    figi: Optional[str] = None
    instrument_id: Optional[str] = None
    candle_source_type: Optional['CandleSource'] = None


    class CandleSource(IntEnum):
        CANDLE_SOURCE_UNSPECIFIED = 0
        CANDLE_SOURCE_EXCHANGE = 1
        CANDLE_SOURCE_INCLUDE_WEEKEND = 3


class CandleInterval(IntEnum):
    CANDLE_INTERVAL_UNSPECIFIED = 0
    CANDLE_INTERVAL_1_MIN = 1
    CANDLE_INTERVAL_5_MIN = 2
    CANDLE_INTERVAL_15_MIN = 3
    CANDLE_INTERVAL_HOUR = 4
    CANDLE_INTERVAL_DAY = 5
    CANDLE_INTERVAL_2_MIN = 6
    CANDLE_INTERVAL_3_MIN = 7
    CANDLE_INTERVAL_10_MIN = 8
    CANDLE_INTERVAL_30_MIN = 9
    CANDLE_INTERVAL_2_HOUR = 10
    CANDLE_INTERVAL_4_HOUR = 11
    CANDLE_INTERVAL_WEEK = 12
    CANDLE_INTERVAL_MONTH = 13


class CandleSource(IntEnum):
    CANDLE_SOURCE_UNSPECIFIED = 0
    CANDLE_SOURCE_EXCHANGE = 1
    CANDLE_SOURCE_DEALER_WEEKEND = 2


@dataclass
class GetCandlesResponse:
    candles: List['HistoricCandle']


@dataclass
class HistoricCandle:
    open: 'Quotation'
    high: 'Quotation'
    low: 'Quotation'
    close: 'Quotation'
    volume: int
    time: datetime
    is_complete: bool
    candle_source: 'CandleSource'


@dataclass
class GetLastPricesRequest:
    figi: List[str]
    instrument_id: List[str]


@dataclass
class GetLastPricesResponse:
    last_prices: List['LastPrice']


@dataclass
class LastPrice:
    figi: str
    price: 'Quotation'
    time: datetime
    instrument_uid: str


@dataclass
class GetOrderBookRequest:
    depth: int
    figi: Optional[str] = None
    instrument_id: Optional[str] = None


@dataclass
class GetOrderBookResponse:
    figi: str
    depth: int
    bids: List['Order']
    asks: List['Order']
    last_price: 'Quotation'
    close_price: 'Quotation'
    limit_up: 'Quotation'
    limit_down: 'Quotation'
    last_price_ts: datetime
    close_price_ts: datetime
    orderbook_ts: datetime
    instrument_uid: str


@dataclass
class GetTradingStatusRequest:
    figi: Optional[str] = None
    instrument_id: Optional[str] = None


@dataclass
class GetTradingStatusesRequest:
    instrument_id: List[str]


@dataclass
class GetTradingStatusesResponse:
    trading_statuses: List['GetTradingStatusResponse']


@dataclass
class GetTradingStatusResponse:
    figi: str
    trading_status: 'SecurityTradingStatus'
    limit_order_available_flag: bool
    market_order_available_flag: bool
    api_trade_available_flag: bool
    instrument_uid: str
    bestprice_order_available_flag: bool
    only_best_price: bool


@dataclass
class GetLastTradesRequest:
    from_: datetime
    to: datetime
    figi: Optional[str] = None
    instrument_id: Optional[str] = None


@dataclass
class GetLastTradesResponse:
    trades: List['Trade']


@dataclass
class GetMySubscriptions:
    pass


@dataclass
class GetClosePricesRequest:
    instruments: List['InstrumentClosePriceRequest']


@dataclass
class InstrumentClosePriceRequest:
    instrument_id: str


@dataclass
class GetClosePricesResponse:
    close_prices: List['InstrumentClosePriceResponse']


@dataclass
class InstrumentClosePriceResponse:
    figi: str
    instrument_uid: str
    price: 'Quotation'
    evening_session_price: 'Quotation'
    time: datetime


@dataclass
class GetTechAnalysisRequest:
    indicator_type: 'IndicatorType'
    instrument_uid: str
    from_: datetime
    to: datetime
    interval: 'IndicatorInterval'
    type_of_price: 'TypeOfPrice'
    length: int
    deviation: 'Deviation'
    smoothing: 'Smoothing'


    @dataclass
    class Smoothing:
        fast_length: int
        slow_length: int
        signal_smoothing: int


    @dataclass
    class Deviation:
        deviation_multiplier: 'Quotation'


    class IndicatorInterval(IntEnum):
        INDICATOR_INTERVAL_UNSPECIFIED = 0
        INDICATOR_INTERVAL_ONE_MINUTE = 1
        INDICATOR_INTERVAL_FIVE_MINUTES = 2
        INDICATOR_INTERVAL_FIFTEEN_MINUTES = 3
        INDICATOR_INTERVAL_ONE_HOUR = 4
        INDICATOR_INTERVAL_ONE_DAY = 5
        INDICATOR_INTERVAL_2_MIN = 6
        INDICATOR_INTERVAL_3_MIN = 7
        INDICATOR_INTERVAL_10_MIN = 8
        INDICATOR_INTERVAL_30_MIN = 9
        INDICATOR_INTERVAL_2_HOUR = 10
        INDICATOR_INTERVAL_4_HOUR = 11
        INDICATOR_INTERVAL_WEEK = 12
        INDICATOR_INTERVAL_MONTH = 13


    class TypeOfPrice(IntEnum):
        TYPE_OF_PRICE_UNSPECIFIED = 0
        TYPE_OF_PRICE_CLOSE = 1
        TYPE_OF_PRICE_OPEN = 2
        TYPE_OF_PRICE_HIGH = 3
        TYPE_OF_PRICE_LOW = 4
        TYPE_OF_PRICE_AVG = 5


    class IndicatorType(IntEnum):
        INDICATOR_TYPE_UNSPECIFIED = 0
        INDICATOR_TYPE_BB = 1
        INDICATOR_TYPE_EMA = 2
        INDICATOR_TYPE_RSI = 3
        INDICATOR_TYPE_MACD = 4
        INDICATOR_TYPE_SMA = 5


@dataclass
class GetTechAnalysisResponse:
    technical_indicators: List['TechAnalysisItem']


    @dataclass
    class TechAnalysisItem:
        timestamp: datetime
        middle_band: Optional['Quotation'] = None
        upper_band: Optional['Quotation'] = None
        lower_band: Optional['Quotation'] = None
        signal: Optional['Quotation'] = None
        macd: Optional['Quotation'] = None


class OrderBookType(IntEnum):
    ORDERBOOK_TYPE_UNSPECIFIED = 0
    ORDERBOOK_TYPE_EXCHANGE = 1
    ORDERBOOK_TYPE_DEALER = 2
