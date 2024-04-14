import requests
from apis.cbbi_fetcher import CBBIFetcher

class CryptoAPI:
  def __init__(self):
    self.BASE_URL = 'https://api.coingecko.com/api/v3'
    self.headers = {
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }

  def get_crypto_price(self, crypto="bitcoin", currency="usd"):
    result = requests.get(f'{self.BASE_URL}/coins/markets?vs_currency={currency}&ids={crypto}&order=id_asc&per_page=100&page=1&sparkline=false&price_change_percentage=1h%2C24h%2C7d%2C%204d%2C30d%2C200d%2C1y', headers=self.headers).json()
    return result.pop().get('current_price')

  def get_crypto_market_chart(self, crypto="bitcoin", currency="usd", days=1):
    if days == "max":
      if crypto == "bitcoin":
        return CBBIFetcher().get_bitcoin_market_chart_max()
      else:
        days = 365
    
    days = int(days)
    if days > 365:
      days = 365
    
    result = requests.get(f'{self.BASE_URL}/coins/{crypto}/market_chart?vs_currency={currency}&days={days}&precision=0', headers=self.headers).json()
    return result