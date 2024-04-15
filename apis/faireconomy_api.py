import requests

class FaireconomyAPI:
  def __init__(self):
    self.BASE_URL = 'https://nfs.faireconomy.media/ff_calendar_thisweek.json'
    self.headers = {
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }
  
  def get_forex_factory_data(self, only_high_impact=True):
    result = requests.get(self.BASE_URL, headers=self.headers).json()
    
    if only_high_impact:
      result = [data for data in result if data.get("impact") in ["High", "Medium"]]
    
    return result
