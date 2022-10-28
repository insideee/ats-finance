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
