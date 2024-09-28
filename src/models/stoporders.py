import datetime


class PostStopOrderRequest:
    figi: str
    quantity: int
    price: 'Quotation'
    stop_price: 'Quotation'
    direction: 'StopOrderDirection'
    account_id: str
    expiration_type: 'StopOrderExpirationType'
    stop_order_type: 'StopOrderType'
    expire_date: datetime
    instrument_id: str
    exchange_order_type: 'ExchangeOrderType'
    take_profit_type: 'TakeProfitType'
    trailing_data: 'TrailingData'
    price_type: 'PriceType'
    order_id: str


    class TrailingData:
        indent: 'Quotation'
        indent_type: 'TrailingValueType'
        spread: 'Quotation'
        spread_type: 'TrailingValueType'


class PostStopOrderResponse:
    stop_order_id: str
    order_request_id: str
    response_metadata: 'ResponseMetadata'


class GetStopOrdersRequest:
    account_id: str
    status: 'StopOrderStatusOption'
    from_: datetime
    to: datetime


class GetStopOrdersResponse:
    stop_orders: 'StopOrder'


class CancelStopOrderRequest:
    account_id: str
    stop_order_id: str


class CancelStopOrderResponse:
    time: datetime


class StopOrder:
    stop_order_id: str
    lots_requested: int
    figi: str
    direction: 'StopOrderDirection'
    currency: str
    order_type: 'StopOrderType'
    create_date: datetime
    activation_date_time: datetime
    expiration_time: datetime
    price: 'MoneyValue'
    stop_price: 'MoneyValue'
    instrument_uid: str
    take_profit_type: 'TakeProfitType'
    trailing_data: 'TrailingData'
    status: 'StopOrderStatusOption'
    exchange_order_type: 'ExchangeOrderType'


    class TrailingData:
        indent: 'Quotation'
        indent_type: 'TrailingValueType'
        spread: 'Quotation'
        spread_type: 'TrailingValueType'
        status: 'TrailingStopStatus'
        price: 'Quotation'
        extr: 'Quotation'


STOP_ORDER_DIRECTION_UNSPECIFIED = 0
STOP_ORDER_DIRECTION_BUY = 1
STOP_ORDER_DIRECTION_SELL = 2
STOP_ORDER_EXPIRATION_TYPE_UNSPECIFIED = 0
STOP_ORDER_EXPIRATION_TYPE_GOOD_TILL_CANCEL = 1
STOP_ORDER_EXPIRATION_TYPE_GOOD_TILL_DATE = 2
STOP_ORDER_TYPE_UNSPECIFIED = 0
STOP_ORDER_TYPE_TAKE_PROFIT = 1
STOP_ORDER_TYPE_STOP_LOSS = 2
STOP_ORDER_TYPE_STOP_LIMIT = 3
STOP_ORDER_STATUS_UNSPECIFIED = 0
STOP_ORDER_STATUS_ALL = 1
STOP_ORDER_STATUS_ACTIVE = 2
STOP_ORDER_STATUS_EXECUTED = 3
STOP_ORDER_STATUS_CANCELED = 4
STOP_ORDER_STATUS_EXPIRED = 5
EXCHANGE_ORDER_TYPE_UNSPECIFIED = 0
EXCHANGE_ORDER_TYPE_MARKET = 1
EXCHANGE_ORDER_TYPE_LIMIT = 2
TAKE_PROFIT_TYPE_UNSPECIFIED = 0
TAKE_PROFIT_TYPE_REGULAR = 1
TAKE_PROFIT_TYPE_TRAILING = 2
TRAILING_VALUE_UNSPECIFIED = 0
TRAILING_VALUE_ABSOLUTE = 1
TRAILING_VALUE_RELATIVE = 2
TRAILING_STOP_UNSPECIFIED = 0
TRAILING_STOP_ACTIVE = 1
TRAILING_STOP_ACTIVATED = 2
