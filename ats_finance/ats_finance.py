"""Ats-finance is an async library for fetch stocks and futures data from polygon api
"""
import yfinance
import aiohttp
import asyncio
from pydantic.error_wrappers import ValidationError
from typing import Optional, Union, List
from pandas import DataFrame

from .enums import Source, PolygonInterval, Polygon, YfinancePeriod, YfinanceInterval
from .exception import (NotAValidSource, NotAValidTicker,
                        MissingRequestArgument, MissingPolygonApiKey,
                        NotAValidIntervalType)
from .config import Settings
from . import utils


class AtsFinance:

    def __init__(self) -> None:
        ...

    @classmethod
    async def _async_request(cls, **kwargs) -> dict:
        """Make the async request"""

        session = kwargs.get('session', None)
        base_url = kwargs.get('base_url', None)
        endpoint = kwargs.get('endpoint', None)
        params = kwargs.get('params', None)
        headers = kwargs.get('headers', None)
        data = kwargs.get('data', None)
        json = kwargs.get('json', None)
        method = kwargs.get('method', None)
        symbol = kwargs.get('symbol', None)

        for arg in [session, base_url, endpoint, method, symbol]:
            if arg is None:
                raise MissingRequestArgument

        try:
            if method == 'GET':
                async with session.get(f'{base_url}{endpoint}', headers=headers, params=params, data=data, json=json) as response:
                    data = await response.json()

                    return {'status_code': response.status,
                            'symbol': symbol,
                            'data': data}

            elif method == 'POST':
                async with session.post(f'{base_url}{endpoint}', headers=headers, params=params, data=data, json=json) as response:
                    data = await response.json()

                    return {'status_code': response.status,
                            'symbol': symbol,
                            'data': data}

            elif method == 'PUT':
                async with session.put(f'{base_url}{endpoint}', headers=headers, params=params, data=data, json=json) as response:
                    data = await response.json()

                    return {'status_code': response.status,
                            'symbol': symbol,
                            'data': data}

            elif method == 'DELETE':
                async with session.delete(f'{base_url}{endpoint}', headers=headers) as response:
                    data = await response.json()

                    return {'status_code': response.status,
                            'symbol': symbol,
                            'data': data}

        except Exception as e:
            return {'status_code': 500,
                    'detail': 'Unable to connect. Try again',
                    'symbol': symbol}

    @classmethod
    async def fetch_raw(cls, ticker: Union[str, list],
                        source: Source,
                        period: Union[int, YfinancePeriod],
                        interval: Union[int, YfinanceInterval],
                        interval_type: Optional[PolygonInterval] = PolygonInterval.MINUTES,
                        api_key: Optional[str] = None) -> tuple | dict:

        if not isinstance(ticker, (list, str)):
            raise NotAValidTicker
        elif not isinstance(source, Source):
            raise NotAValidSource

        if source.value == 'polygon':

            if not api_key:
                try:
                    settings = Settings()
                    api_key = settings.polygon_key
                except ValidationError:
                    raise MissingPolygonApiKey

            end_period, start_period = utils.get_period_interval(period)
            base_url = Polygon.URL.value
            endpoints = list()

            if type(ticker) == str:
                ticker = [ticker]

            for t in ticker:
                endpoints.append(
                    f'{Polygon.TICKER_ENDPOINT.value}{t}/range/{interval}/{interval_type.value}/{start_period}/{end_period}?adjusted=false&limit=50000&sort=asc&apiKey={api_key}')

            async with aiohttp.ClientSession() as session:
                tasks = [cls._async_request(session=session,
                                            base_url=base_url,
                                            endpoint=endpoints[i],
                                            method='GET',
                                            symbol=t) for i, t in enumerate(ticker)]

                return await asyncio.gather(*tasks)



    @classmethod
    async def yf_ticker_history(cls, ticker: str,
                                period: YfinancePeriod = YfinancePeriod.WEEK,
                                interval: YfinanceInterval = YfinanceInterval.ONE_MINUTE):
        obj = yfinance.Ticker(ticker)

        return obj.history(period=period.value, interval=interval.value,
                           start=None, end=None, prepost=False, actions=True,
                           auto_adjust=True, back_adjust=False,
                           proxy=None, rounding=False, timeout=None)
        
        
    @classmethod    
    def yfinance_fetch(cls, ticker: list,
                    period: Union[int, YfinancePeriod],
                    interval: Union[int, YfinanceInterval],
                    local_timezone: bool = False,
                    source: Source = Source.YFINANCE) -> List[dict]: 
        
        
        df = yfinance.download(tickers=ticker,
                                       period=period.value,
                                       interval=interval.value,
                                       auto_adjust=False,
                                       progress=False)
        aux = dict()
        aux['symbol'] = ticker[i]
        aux['df'] = df.reset_index()
        aux['df'] = aux['df'][['Datetime', 'Open', 'High', 'Low', 'Close', 'Volume']]
        
        return [aux]


    @classmethod
    async def fetch(cls, ticker: Union[str, list],
                    source: Source,
                    period: Union[int, YfinancePeriod],
                    interval: Union[int, YfinanceInterval],
                    local_timezone: bool = False,
                    interval_type: Optional[PolygonInterval] = PolygonInterval.MINUTES,
                    api_key: Optional[str] = None) -> List[dict]:
        """Fetch aggregates data for a ticker or a list of them

        Args:
            ticker (Union[str, list]): A single ticker or a list of them.
            source (Source): Source for fetch data from (Only supports polygon for now)
            period (int): Time period (in days) to fetch the data.
            interval (int): Aggregate bar interval value.
            local_timezone (bool, optional): Defines if the datetime column
                                             will be converted to local tz. Defaults to False.
            interval_type (PolygonInterval, optional): Enum for interval type. Defaults to PolygonInterval.MINUTES.
            api_key (Optional[str], optional): If you don't define any, it will look for an
                                              .env file with the variable 'polygon_key'. Defaults to None.

        Returns:
            List[dict]: It will return a list of dictionaries with the following schema:
            {'symbol': str,
             'df': pandas.Dataframe}
            
        """

        data = await cls.fetch_raw(ticker=ticker,
                                   source=source,
                                   period=period,
                                   interval=interval,
                                   interval_type=interval_type,
                                   api_key=api_key)

        dataframes = list()

        for result in data:
            if result['status_code'] == 200 and result['data']['resultsCount'] > 0:
                df_raw = DataFrame(data=result['data']['results'])
                df = df_raw.rename(columns={'v': 'Volume',
                                            'vw': 'Volume weighted',
                                            'o': 'Open',
                                            'h': 'High',
                                            'l': 'Low',
                                            'c': 'Close',
                                            't': 'Timestamp',
                                            'n': 'Window Agg Transactions'})

                df['Datetime'] = utils.to_datetime(series=df.Timestamp,
                                                   source=Source.POLYGON,
                                                   local_timezone=local_timezone)
                aux = dict()
                aux['symbol'] = result['symbol']
                aux['df'] = df
                dataframes.append(aux)

        return dataframes
