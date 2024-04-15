import requests
import json
from datetime import datetime, timedelta
import math

class CBBIFetcher:
  def __init__(self):
    self.BASE_URL = 'https://colintalkscrypto.com/cbbi/data/latest.json'
    self.headers = {
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }
    
  def fetch_cbbi_data(self):
    now = datetime.now()
    today = datetime(now.year, now.month, now.day, 2, 0, 0)
    today_timestamp = int(today.timestamp())

    cbbi_data = {}
    
    with open("data/cbbi_data.json", "r") as f:
      data = f.read()
      if data:
        cbbi_data = json.loads(data)
                
        if str(list(cbbi_data.get("Confidence").keys())[-1]) == str(today_timestamp):
          print("Using cached data")
          return cbbi_data
                
    print("Fetching new data")
    result = requests.get(self.BASE_URL, headers=self.headers).json()
    with open("data/cbbi_data.json", "w") as f:
      json.dump(result, f)
    
    return result
  
  def get_bitcoin_market_chart_max(self):
    return self.format_price_range(self.fetch_cbbi_data()["Price"])
    
  def format_price_range(self, data):
    formatted_data = []
    
    for key, value in data.items():
      formatted_data.append([int(key), int(value)])
      
    return {
      "prices": formatted_data
    }
  def get_cbbi(self, days=1):
    cbbi_history = self.fetch_cbbi_data()["Confidence"]

    cbbi_history_array = list(cbbi_history.values())
    cbbi_history_array = cbbi_history_array[-int(days):]
    cbbi_history_array = [round(value * 100, 2) for value in cbbi_history_array]
    cbbi_history_array.reverse()

    return cbbi_history_array