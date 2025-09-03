# remote jobs feed
import requests
import json


url = "https://jobicy.com/api/v2/remote-jobs?count=25&geo=australia&industry=dev"
data_req = requests.get(url)
data_json = data_req.json()
print(data_json)
print("")

'''
if 'pubDate' in data_json:
  live_data = data_json['pubDate']
  print(f'live data: {live_data}')
else:
  print("live data not found in the api response")
'''