from datetime import datetime, timedelta
from pandas import Series
from .enums import Source
from dateutil import tz


def get_period_interval(period_days: int) -> list:
    """Return the star and end date for a given period of days"""

    end_raw = datetime.now()
    start_raw = end_raw - timedelta(days=period_days)
    end = end_raw.strftime('%Y-%m-%d')
    start = start_raw.strftime('%Y-%m-%d')

    return [end, start]


def _to_local(date: datetime):
    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()

    date = date.replace(tzinfo=from_zone)
    return date.astimezone(to_zone)


def to_datetime(series: Series, source: Source, local_timezone: bool = False) -> Series:
    a = series.copy() / 1000 if source == Source.POLYGON else series.copy()
    a = a.map(datetime.utcfromtimestamp)
    if local_timezone:
        a = a.map(_to_local)

    return a
