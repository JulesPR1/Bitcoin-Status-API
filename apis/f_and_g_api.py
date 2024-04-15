import requests

class FGAPI:
  def __init__(self):
    self.BASE_URL = 'https://api.alternative.me/fng/'
    self.headers = {
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }
  
  def get_fng(self, days=1):
    result = requests.get(f'{self.BASE_URL}?limit={days}', headers=self.headers).json()
    return result
  
  def get_fng_simple(self, days=1):
    result = self.get_fng(days)
    return [data.get("value") for data in result.get("data")]
