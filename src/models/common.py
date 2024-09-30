from enum import Enum
from enum import Enum
from enum import Enum
from enum import Enum
import datetime


class InstrumentType(Enum):
    INSTRUMENT_TYPE_UNSPECIFIED = 0
    INSTRUMENT_TYPE_BOND = 1
    INSTRUMENT_TYPE_SHARE = 2
    INSTRUMENT_TYPE_CURRENCY = 3
    INSTRUMENT_TYPE_ETF = 4
    INSTRUMENT_TYPE_FUTURES = 5
    INSTRUMENT_TYPE_SP = 6
    INSTRUMENT_TYPE_OPTION = 7
    INSTRUMENT_TYPE_CLEARING_CERTIFICATE = 8
    INSTRUMENT_TYPE_INDEX = 9
    INSTRUMENT_TYPE_COMMODITY = 10


class MoneyValue:
    currency: str
    units: int
    nano: int


class Quotation:
    units: int
    nano: int


class SecurityTradingStatus(Enum):
    SECURITY_TRADING_STATUS_UNSPECIFIED = 0
    SECURITY_TRADING_STATUS_NOT_AVAILABLE_FOR_TRADING = 1
    SECURITY_TRADING_STATUS_OPENING_PERIOD = 2
    SECURITY_TRADING_STATUS_CLOSING_PERIOD = 3
    SECURITY_TRADING_STATUS_BREAK_IN_TRADING = 4
    SECURITY_TRADING_STATUS_NORMAL_TRADING = 5
    SECURITY_TRADING_STATUS_CLOSING_AUCTION = 6
    SECURITY_TRADING_STATUS_DARK_POOL_AUCTION = 7
    SECURITY_TRADING_STATUS_DISCRETE_AUCTION = 8
    SECURITY_TRADING_STATUS_OPENING_AUCTION_PERIOD = 9
    SECURITY_TRADING_STATUS_TRADING_AT_CLOSING_AUCTION_PRICE = 10
    SECURITY_TRADING_STATUS_SESSION_ASSIGNED = 11
    SECURITY_TRADING_STATUS_SESSION_CLOSE = 12
    SECURITY_TRADING_STATUS_SESSION_OPEN = 13
    SECURITY_TRADING_STATUS_DEALER_NORMAL_TRADING = 14
    SECURITY_TRADING_STATUS_DEALER_BREAK_IN_TRADING = 15
    SECURITY_TRADING_STATUS_DEALER_NOT_AVAILABLE_FOR_TRADING = 16


class Ping:
    time: datetime
    stream_id: str


class PriceType(Enum):
    PRICE_TYPE_UNSPECIFIED = 0
    PRICE_TYPE_POINT = 1
    PRICE_TYPE_CURRENCY = 2


class Page:
    limit: int
    page_number: int


class PageResponse:
    limit: int
    page_number: int
    total_count: int


class ResponseMetadata:
    tracking_id: str
    server_time: datetime


class BrandData:
    logo_name: str
    logo_base_color: str
    text_color: str


class ResultSubscriptionStatus(Enum):
    RESULT_SUBSCRIPTION_STATUS_UNSPECIFIED = 0
    RESULT_SUBSCRIPTION_STATUS_OK = 1
    RESULT_SUBSCRIPTION_STATUS_ERROR = 13


class ErrorDetail:
    code: str
    message: str
