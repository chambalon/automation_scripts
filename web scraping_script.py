import requests
from bs4 import BeautifulSoup


url = "https://www.bbc.com/news"
response = requests.get(url)

if response.status_code == 200:
  soup_content = BeautifulSoup(response.content, 'html.parser')
  titles = soup_content.find_all('h2')
  for title in titles:
    print(title.text)
  para = soup_content.select_one('p').text
  print(f'Para: {para}')
else:
  print(f"Failed to retrieve the page. Status code: {response.status_code}")
  