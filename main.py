from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from apis.crypto_api import CryptoAPI
from apis.cbbi_fetcher import CBBIFetcher

app = FastAPI()


@app.get("/", include_in_schema=False)
def doc():
  return RedirectResponse(url='/docs')

@app.get("/crypto-price")
def get_crypto_price(crypto="bitcoin", currency="usd"):
  """
  Display current crypto price
  
  Update Frequency: every 60 seconds
  """
  return CryptoAPI().get_crypto_price(crypto, currency)

@app.get("/crypto-market-chart")
def get_crypto_market_chart(crypto="bitcoin", currency="usd", days=1):
  """
  Get historical market data include price, market cap, and 24h volume

  - 1 day from current time = 5 minute interval data
  - 2 - 90 days from current time = hourly data
  - above 90 days from current time = daily data (00:00 UTC)
  - max days = since 2011

  Cache based on days range:

  - 1 day = 30 seconds cache
  - 2-90 days = 30 minutes cache
  - 90 days = 12 hours cache
  
  Anything above 365 days will return max days data (since 2011)
  """
  return CryptoAPI().get_crypto_market_chart(crypto, currency, days)
