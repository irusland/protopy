from enum import Enum
import datetime


class MarketDataRequest:
    pass


class MarketDataServerSideStreamRequest:
    subscribe_candles_request: 'SubscribeCandlesRequest'
    subscribe_order_book_request: 'SubscribeOrderBookRequest'
    subscribe_trades_request: 'SubscribeTradesRequest'
    subscribe_info_request: 'SubscribeInfoRequest'
    subscribe_last_price_request: 'SubscribeLastPriceRequest'


class MarketDataResponse:
    pass


class SubscribeCandlesRequest:
    subscription_action: 'SubscriptionAction'
    instruments: 'CandleInstrument'
    waiting_close: 'bool'


class SubscriptionAction(Enum):
    SUBSCRIPTION_ACTION_UNSPECIFIED = 0
    SUBSCRIPTION_ACTION_SUBSCRIBE = 1
    SUBSCRIPTION_ACTION_UNSUBSCRIBE = 2


class SubscriptionInterval(Enum):
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


class CandleInstrument:
    figi: str
    interval: 'SubscriptionInterval'
    instrument_id: str


class SubscribeCandlesResponse:
    tracking_id: str
    candles_subscriptions: 'CandleSubscription'


class CandleSubscription:
    figi: str
    interval: 'SubscriptionInterval'
    subscription_status: 'SubscriptionStatus'
    instrument_uid: str
    waiting_close: 'bool'
    stream_id: str
    subscription_id: str


class SubscriptionStatus(Enum):
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


class SubscribeOrderBookRequest:
    subscription_action: 'SubscriptionAction'
    instruments: 'OrderBookInstrument'


class OrderBookInstrument:
    figi: str
    depth: int
    instrument_id: str
    order_book_type: 'OrderBookType'


class SubscribeOrderBookResponse:
    tracking_id: str
    order_book_subscriptions: 'OrderBookSubscription'


class OrderBookSubscription:
    figi: str
    depth: int
    subscription_status: 'SubscriptionStatus'
    instrument_uid: str
    stream_id: str
    subscription_id: str
    order_book_type: 'OrderBookType'


class TradeSourceType(Enum):
    TRADE_SOURCE_UNSPECIFIED = 0
    TRADE_SOURCE_EXCHANGE = 1
    TRADE_SOURCE_DEALER = 2
    TRADE_SOURCE_ALL = 3


class SubscribeTradesRequest:
    subscription_action: 'SubscriptionAction'
    instruments: 'TradeInstrument'
    trade_type: 'TradeSourceType'


class TradeInstrument:
    figi: str
    instrument_id: str


class SubscribeTradesResponse:
    tracking_id: str
    trade_subscriptions: 'TradeSubscription'
    trade_type: 'TradeSourceType'


class TradeSubscription:
    figi: str
    subscription_status: 'SubscriptionStatus'
    instrument_uid: str
    stream_id: str
    subscription_id: str


class SubscribeInfoRequest:
    subscription_action: 'SubscriptionAction'
    instruments: 'InfoInstrument'


class InfoInstrument:
    figi: str
    instrument_id: str


class SubscribeInfoResponse:
    tracking_id: str
    info_subscriptions: 'InfoSubscription'


class InfoSubscription:
    figi: str
    subscription_status: 'SubscriptionStatus'
    instrument_uid: str
    stream_id: str
    subscription_id: str


class SubscribeLastPriceRequest:
    subscription_action: 'SubscriptionAction'
    instruments: 'LastPriceInstrument'


class LastPriceInstrument:
    figi: str
    instrument_id: str


class SubscribeLastPriceResponse:
    tracking_id: str
    last_price_subscriptions: 'LastPriceSubscription'


class LastPriceSubscription:
    figi: str
    subscription_status: 'SubscriptionStatus'
    instrument_uid: str
    stream_id: str
    subscription_id: str


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


class OrderBook:
    figi: str
    depth: int
    is_consistent: 'bool'
    bids: 'Order'
    asks: 'Order'
    time: datetime
    limit_up: 'Quotation'
    limit_down: 'Quotation'
    instrument_uid: str
    order_book_type: 'OrderBookType'


class Order:
    price: 'Quotation'
    quantity: int


class Trade:
    figi: str
    direction: 'TradeDirection'
    price: 'Quotation'
    quantity: int
    time: datetime
    instrument_uid: str
    tradeSource: 'TradeSourceType'


class TradeDirection(Enum):
    TRADE_DIRECTION_UNSPECIFIED = 0
    TRADE_DIRECTION_BUY = 1
    TRADE_DIRECTION_SELL = 2


class TradingStatus:
    figi: str
    trading_status: 'SecurityTradingStatus'
    time: datetime
    limit_order_available_flag: 'bool'
    market_order_available_flag: 'bool'
    instrument_uid: str


class GetCandlesRequest:
    figi: str
    from_: datetime
    to: datetime
    interval: 'CandleInterval'
    instrument_id: str
    candle_source_type: 'CandleSource'


    class CandleSource(Enum):
        CANDLE_SOURCE_UNSPECIFIED = 0
        CANDLE_SOURCE_EXCHANGE = 1
        CANDLE_SOURCE_INCLUDE_WEEKEND = 3


class CandleInterval(Enum):
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


class CandleSource(Enum):
    CANDLE_SOURCE_UNSPECIFIED = 0
    CANDLE_SOURCE_EXCHANGE = 1
    CANDLE_SOURCE_DEALER_WEEKEND = 2


class GetCandlesResponse:
    candles: 'HistoricCandle'


class HistoricCandle:
    open: 'Quotation'
    high: 'Quotation'
    low: 'Quotation'
    close: 'Quotation'
    volume: int
    time: datetime
    is_complete: 'bool'
    candle_source: 'CandleSource'


class GetLastPricesRequest:
    figi: str
    instrument_id: str


class GetLastPricesResponse:
    last_prices: 'LastPrice'


class LastPrice:
    figi: str
    price: 'Quotation'
    time: datetime
    instrument_uid: str


class GetOrderBookRequest:
    figi: str
    depth: int
    instrument_id: str


class GetOrderBookResponse:
    figi: str
    depth: int
    bids: 'Order'
    asks: 'Order'
    last_price: 'Quotation'
    close_price: 'Quotation'
    limit_up: 'Quotation'
    limit_down: 'Quotation'
    last_price_ts: datetime
    close_price_ts: datetime
    orderbook_ts: datetime
    instrument_uid: str


class GetTradingStatusRequest:
    figi: str
    instrument_id: str


class GetTradingStatusesRequest:
    instrument_id: str


class GetTradingStatusesResponse:
    trading_statuses: 'GetTradingStatusResponse'


class GetTradingStatusResponse:
    figi: str
    trading_status: 'SecurityTradingStatus'
    limit_order_available_flag: 'bool'
    market_order_available_flag: 'bool'
    api_trade_available_flag: 'bool'
    instrument_uid: str
    bestprice_order_available_flag: 'bool'
    only_best_price: 'bool'


class GetLastTradesRequest:
    figi: str
    from_: datetime
    to: datetime
    instrument_id: str


class GetLastTradesResponse:
    trades: 'Trade'


class GetMySubscriptions:
    pass


class GetClosePricesRequest:
    instruments: 'InstrumentClosePriceRequest'


class InstrumentClosePriceRequest:
    instrument_id: str


class GetClosePricesResponse:
    close_prices: 'InstrumentClosePriceResponse'


class InstrumentClosePriceResponse:
    figi: str
    instrument_uid: str
    price: 'Quotation'
    evening_session_price: 'Quotation'
    time: datetime


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


    class Smoothing:
        fast_length: int
        slow_length: int
        signal_smoothing: int


    class Deviation:
        deviation_multiplier: 'Quotation'


    class IndicatorInterval(Enum):
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


    class TypeOfPrice(Enum):
        TYPE_OF_PRICE_UNSPECIFIED = 0
        TYPE_OF_PRICE_CLOSE = 1
        TYPE_OF_PRICE_OPEN = 2
        TYPE_OF_PRICE_HIGH = 3
        TYPE_OF_PRICE_LOW = 4
        TYPE_OF_PRICE_AVG = 5


    class IndicatorType(Enum):
        INDICATOR_TYPE_UNSPECIFIED = 0
        INDICATOR_TYPE_BB = 1
        INDICATOR_TYPE_EMA = 2
        INDICATOR_TYPE_RSI = 3
        INDICATOR_TYPE_MACD = 4
        INDICATOR_TYPE_SMA = 5


class GetTechAnalysisResponse:
    technical_indicators: 'TechAnalysisItem'


    class TechAnalysisItem:
        timestamp: datetime
        middle_band: 'Quotation'
        upper_band: 'Quotation'
        lower_band: 'Quotation'
        signal: 'Quotation'
        macd: 'Quotation'


class OrderBookType(Enum):
    ORDERBOOK_TYPE_UNSPECIFIED = 0
    ORDERBOOK_TYPE_EXCHANGE = 1
    ORDERBOOK_TYPE_DEALER = 2
