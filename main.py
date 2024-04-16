from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from apis.crypto_api import CryptoAPI
from apis.cbbi_fetcher import CBBIFetcher
from apis.f_and_g_api import FGAPI
from apis.faireconomy_api import FaireconomyAPI
from apis.coin_telegraph_rss_reader import CoinTelegraphRssReader


tags_metadata = [
    {
      "name": "cryptocurrency",
      "description": "Get cryptocurrency price",
    },
    {
      "name": "indexes",
      "description": "Get Indexes about Bitcoin",
    },
    {
      "name": "events",
      "description": "Get upcomming events from Forex Factory"
    },
    {
      "name": "news",
      "description": "Get latest news from CoinTelegraph RSS Feed"
    }
]


app = FastAPI(openapi_tags=tags_metadata)


@app.get("/", include_in_schema=False)
def doc():
  return RedirectResponse(url='/docs')

@app.get("/crypto-price", tags=["cryptocurrency"])
def get_crypto_price(crypto="bitcoin", currency="usd"):
  """
  Display current crypto price
  
  Update Frequency: every 60 seconds
  """
  return CryptoAPI().get_crypto_price(crypto, currency)

@app.get("/crypto-market-chart", tags=["cryptocurrency"])
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

@app.get("/fng", tags=["indexes"])
def get_fng(days=1):
  """
  Get Fear and Greed Index
  
  First value is the most recent one
  
  Update Frequency: everyday at 00:00 UTC
  """
  return FGAPI().get_fng_simple(days)

@app.get("/cbbi", tags=["indexes"])
def get_cbbi(days=1):
  """
  Get CBBI
  
  First value is the most recent one

  Update Frequency: everyday at 00:00 UTC
  """
  return CBBIFetcher().get_cbbi(days)

@app.get("/upcomming-events", tags=["events"])
def get_upcomming_events(currencies="USD,EUR", only_high_impact=False):
  """
  Get upcomming week events from Forex Factory
  
  Update Frequency: everyday at 00:00 UTC
  """
  return FaireconomyAPI().get_forex_factory_data(currencies, only_high_impact)

@app.get("/available-currencies", tags=["events"])
def get_available_currencies():
  """
  Get available currencies for Forex Factory events
  """
  return FaireconomyAPI().get_available_currencies()

@app.get("/news", tags=["news"])
def get_news():
  """
  Get latest news from CoinTelegraph
  
  Update Frequency: every 5 minutes
  """
  return CoinTelegraphRssReader().get_news()