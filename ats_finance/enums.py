from enum import Enum


class Source(Enum):

    POLYGON = 'polygon'
    YFINANCE = 'yfinance'


class ApiUrl(Enum):

    YFINANCE = 'https://query1.finance.yahoo.com/v8/finance/chart/'


class Polygon(Enum):

    URL = 'https://api.polygon.io/'
    TICKER_ENDPOINT = 'v2/aggs/ticker/'


class PolygonInterval(Enum):

    MINUTES = 'minute'
    HOUR = 'hour'
    WEEK = 'week'
    DAY = 'day'
    MONTH = 'month'
    YEAR = 'year'


class YfinancePeriod(Enum):

    WEEK = '7d'
    MONTH = '1mo'


class YfinanceInterval(Enum):

    ONE_MINUTE = '1m'
    TWO_MINUTES = '2m'
    FIVE_MINUTES = '5m'
    FIFTEEN_MINUTES = '15m'
    THIRTY_MINUTES = '30m'
    SIXTH_MINUTES = '60m'
    ONE_HOUR = '1h'
    ONE_DAY = '1d'
    FIVE_DAYS = '5d'
    ONE_WEEK = '1wk'
    ONE_MONTH = '1mo'
    THREE_MINUTE = '3mo'
