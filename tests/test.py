import pytest
from ats_finance import AtsFinance, Source, exception, utils
import os


@pytest.mark.asyncio
async def test_ticker_exception():
    """Test the ticker exception"""

    with pytest.raises(exception.NotAValidTicker):
        await AtsFinance.fetch_raw(ticker=1, source=Source.POLYGON,
                                   period=30, interval=60)
        await AtsFinance.fetch_raw(ticker={'test': 'test'}, source=Source.POLYGON,
                                   period=30, interval=60)
        await AtsFinance.fetch(ticker=1, source=Source.POLYGON,
                               period=30, interval=60)
        await AtsFinance.fetch(ticker={'test': 'test'}, source=Source.POLYGON,
                               period=30, interval=60)


@pytest.mark.asyncio
async def test_source_exception():
    """Test the source exception"""

    with pytest.raises(exception.NotAValidSource):
        await AtsFinance.fetch_raw(ticker='TEST', source='',
                                   period=30, interval=60)
        await AtsFinance.fetch_raw(ticker='TEST',
                                   source=[Source.POLYGON, Source.YFINANCE],
                                   period=30, interval=60)
        await AtsFinance.fetch(ticker='TEST', source='',
                               period=30, interval=60)
        await AtsFinance.fetch(ticker='TEST',
                               source=[Source.POLYGON, Source.YFINANCE],
                               period=30, interval=60)


@pytest.mark.skipif(os.path.isfile(os.path.join(os.getcwd(), '.env')),
                    reason='Env file exists, for this test delete it first')
@pytest.mark.asyncio
async def test_api_key_exception():
    """Test the api key exception without a .env file"""

    with pytest.raises(exception.MissingPolygonApiKey):
        await AtsFinance.fetch_raw(ticker='TEST', source=Source.POLYGON,
                                   period=30, interval=60)


@pytest.mark.asyncio
@pytest.mark.skip(reason="Speed test, comment this out if you want to test it")
async def test_with_503_tickers():
    """Test the async request speed with 503 tickers,
    use --durations=value and --vv as pytest argument"""
    tickers = ['A', 'AAL', 'AAP', 'AAPL', 'ABBV', 'ABC', 'ABMD', 'ABT', 'ACN', 'ADBE',
               'ADI', 'ADM', 'ADP', 'ADSK', 'AEE', 'AEP', 'AES', 'AFL', 'AIG', 'AIZ', 'AJG',
               'AKAM', 'ALB', 'ALGN', 'ALK', 'ALL', 'ALLE', 'AMAT', 'AMCR', 'AMD', 'AME',
               'AMGN', 'AMP', 'AMT', 'AMZN', 'ANET', 'ANSS', 'AON', 'AOS', 'APA', 'APD',
               'APH', 'APTV', 'ARE', 'ATO', 'ATVI', 'AVB', 'AVGO', 'AVY', 'AWK', 'AXP',
               'AZO', 'BA', 'BAC', 'BALL', 'BAX', 'BBWI', 'BBY', 'BDX', 'BEN', 'BF.B',
               'BIIB', 'BIO', 'BK', 'BKNG', 'BKR', 'BLK', 'BMY', 'BR', 'BRK.B', 'BRO', 'BSX',
               'BWA', 'BXP', 'C', 'CAG', 'CAH', 'CARR', 'CAT', 'CB', 'CBOE', 'CBRE', 'CCI', 'CCL',
               'CDAY', 'CDNS', 'CDW', 'CE', 'CEG', 'CF', 'CFG', 'CHD', 'CHRW', 'CHTR', 'CI', 'CINF',
               'CL', 'CLX', 'CMA', 'CMCSA', 'CME', 'CMG', 'CMI', 'CMS', 'CNC', 'CNP', 'COF', 'COO',
               'COP', 'COST', 'CPB', 'CPRT', 'CPT', 'CRL', 'CRM', 'CSCO', 'CSGP', 'CSX', 'CTAS',
               'CTLT', 'CTRA', 'CTSH', 'CTVA', 'CVS', 'CVX', 'CZR', 'D', 'DAL', 'DD', 'DE', 'DFS',
               'DG', 'DGX', 'DHI', 'DHR', 'DIS', 'DISH', 'DLR', 'DLTR', 'DOV', 'DOW', 'DPZ', 'DRI',
               'DTE', 'DUK', 'DVA', 'DVN', 'DXC', 'DXCM', 'EA', 'EBAY', 'ECL', 'ED', 'EFX', 'EIX', 'EL', 'ELV',
               'EMN', 'EMR', 'ENPH', 'EOG', 'EPAM', 'EQIX', 'EQR', 'EQT', 'ES', 'ESS', 'ETN', 'ETR', 'ETSY', 'EVRG',
               'EW', 'EXC', 'EXPD', 'EXPE', 'EXR', 'F', 'FANG', 'FAST', 'FBHS', 'FCX', 'FDS', 'FDX', 'FE', 'FFIV', 'FIS',
               'FISV', 'FITB', 'FLT', 'FMC', 'FOX', 'FOXA', 'FRC', 'FRT', 'FTNT', 'FTV', 'GD', 'GE', 'GILD', 'GIS', 'GL',
               'GLW', 'GM', 'GNRC', 'GOOG', 'GOOGL', 'GPC', 'GPN', 'GRMN', 'GS', 'GWW', 'HAL', 'HAS', 'HBAN', 'HCA', 'HD',
               'HES', 'HIG', 'HII', 'HLT', 'HOLX', 'HON', 'HPE', 'HPQ', 'HRL', 'HSIC', 'HST', 'HSY', 'HUM', 'HWM', 'IBM',
               'ICE', 'IDXX', 'IEX', 'IFF', 'ILMN', 'INCY', 'INTC', 'INTU', 'INVH', 'IP', 'IPG', 'IQV', 'IR', 'IRM', 'ISRG',
               'IT', 'ITW', 'IVZ', 'J', 'JBHT',
               'JCI', 'JKHY', 'JNJ', 'JNPR', 'JPM', 'K', 'KDP', 'KEY', 'KEYS', 'KHC',
               'KIM', 'KLAC', 'KMB', 'KMI', 'KMX', 'KO', 'KR', 'L', 'LDOS', 'LEN', 'LH',
               'LHX', 'LIN', 'LKQ', 'LLY', 'LMT', 'LNC', 'LNT', 'LOW', 'LRCX', 'LUMN',
               'LUV', 'LVS', 'LW', 'LYB', 'LYV', 'MA', 'MAA', 'MAR', 'MAS', 'MCD',
               'MCHP', 'MCK', 'MCO', 'MDLZ', 'MDT', 'MET', 'META', 'MGM', 'MHK',
               'MKC', 'MKTX', 'MLM', 'MMC', 'MMM', 'MNST', 'MO', 'MOH', 'MOS',
               'MPC', 'MPWR', 'MRK', 'MRNA', 'MRO', 'MS', 'MSCI', 'MSFT', 'MSI',
               'MTB', 'MTCH', 'MTD', 'MU', 'NCLH', 'NDAQ', 'NDSN', 'NEE', 'NEM',
               'NFLX', 'NI', 'NKE', 'NLOK', 'NOC', 'NOW', 'NRG', 'NSC', 'NTAP',
               'NTRS', 'NUE', 'NVDA', 'NVR', 'NWL', 'NWS', 'NWSA', 'NXPI', 'O',
               'ODFL', 'OGN', 'OKE', 'OMC', 'ON', 'ORCL', 'ORLY', 'OTIS', 'OXY',
               'PARA', 'PAYC', 'PAYX', 'PCAR', 'PCG', 'PEAK', 'PEG', 'PEP', 'PFE',
               'PFG', 'PG', 'PGR', 'PH', 'PHM', 'PKG', 'PKI', 'PLD', 'PM', 'PNC',
               'PNR', 'PNW', 'POOL', 'PPG', 'PPL', 'PRU', 'PSA', 'PSX', 'PTC', 'PWR', 'PXD',
               'PYPL', 'QCOM', 'QRVO', 'RCL', 'RE', 'REG', 'REGN', 'RF', 'RHI', 'RJF', 'RL', 'RMD',
               'ROK', 'ROL', 'ROP', 'ROST', 'RSG', 'RTX', 'SBAC', 'SBNY', 'SBUX', 'SCHW', 'SEDG', 'SEE',
               'SHW', 'SIVB', 'SJM', 'SLB', 'SNA', 'SNPS', 'SO', 'SPG', 'SPGI', 'SRE', 'STE', 'STT', 'STX',
               'STZ', 'SWK', 'SWKS', 'SYF', 'SYK', 'SYY', 'T', 'TAP', 'TDG', 'TDY', 'TECH', 'TEL', 'TER',
               'TFC', 'TFX', 'TGT', 'TJX', 'TMO', 'TMUS', 'TPR', 'TRGP', 'TRMB', 'TROW', 'TRV',
               'TSCO', 'TSLA', 'TSN', 'TT', 'TTWO', 'TWTR', 'TXN', 'TXT', 'TYL', 'UAL',
               'UDR', 'UHS', 'ULTA', 'UNH', 'UNP', 'UPS', 'URI', 'USB', 'V', 'VFC', 'VICI', 'VLO', 'VMC',
               'VNO', 'VRSK', 'VRSN', 'VRTX', 'VTR', 'VTRS', 'VZ', 'WAB', 'WAT', 'WBA', 'WBD', 'WDC',
               'WEC', 'WELL', 'WFC', 'WHR', 'WM', 'WMB', 'WMT', 'WRB', 'WRK', 'WST', 'WTW', 'WY', 'WYNN',
               'XEL', 'XOM', 'XRAY', 'XYL', 'YUM', 'ZBH', 'ZBRA', 'ZION', 'ZTS']
    tickers_b = ['A', 'AAL', 'AAP', 'AAPL', 'ABBV', 'ABC', 'ABMD', 'ABT', 'ACN', 'ADBE']
    data = await AtsFinance.fetch_raw(ticker=tickers_b, source=Source.POLYGON,
                                      period=30, interval=60)

    assert len(data) == len(tickers_b)


@pytest.mark.asyncio
async def test_dataframe_response():
    ticker = ['AAPL', 'AMZN', 'ANET', 'ANSS']
    df = await AtsFinance.fetch(ticker=ticker, source=Source.POLYGON,
                                period=30, interval=60)

    equals = False
    for d in df:
        for t in ticker:
            if d['symbol'] == t:
                equals = True
                break

    if not equals:
        assert False


@pytest.mark.asyncio
async def test_dataframe_scheme():
    ticker = ['AAPL']
    df = await AtsFinance.fetch(ticker=ticker, source=Source.POLYGON,
                                period=30, interval=60)
    columns = ['Open', 'Close', 'High', 'Low', 'Volume', 'Volume weighted', 'Window Agg Transactions', 'Timestamp']
    c = df[0]['df'].columns

    for c_ in columns:
        assert c_ in c


