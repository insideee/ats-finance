
# ATS Finance

ATS Finance is a async library for fetch stock and futures data from polygon api.




## Instalation

```bash
  pip install git+https://git.apathetic.app/Apathetic/ATS-Finance.git
```
    
## Basic usage

```python
  from ats_finance import AtsFinance, Source
  import asyncio
  import platform

  if __name__ == '__main__':
    
      if platform.system() == 'Windows':
          asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
      data = asyncio.run(AtsFinance.fetch(ticker=['AAPL'],                             # list of tickers
                                          source=Source.POLYGON,                       # api source to be used
                                          period=30,                                   # time period (in days) to fetch the data
                                          interval=60,                                 # aggregates interval (in minutes)
                                          local_timezone=False,                        # convert to local timezone
                                          api_key='YOUR_POLYGON_KEY'))                 # polygon api key
    
    print(data[0]['df'])

```


## Reference

 - [Apathetic Trading System](https://apathetic.ai/)
 - [Polygon Api](https://polygon.io/)


## Authors

- [@insideee](https://www.github.com/insideee)

