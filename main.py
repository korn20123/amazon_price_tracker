import json
import time
import requests
from bs4 import BeautifulSoup
with open('settings.json', 'r') as f:
  settings = json.load(f)
URL = settings["url"]
budget = float(settings["budget"])
apikey = settings["apikey"]
phone = settings["phone"]
time_wait = int(settings["time_wait"])
def check_amazon_price():
  headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'} 
  try:
    print('checking price...')
    response = requests.get(URL, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find('span', id="productTitle").getText()
    price_str = soup.find('span', class_="a-offscreen").getText()
    price_clean =price_str.replace('.', '').replace(',', '.').replace('€', '').replace(' ', '').strip()
    price = float(price_clean)
    return price, title
  except Exception as e:
    print(e)
def send_to_whatsapp(message):
  url = f'https://api.callmebot.com/whatsapp.php?phone={phone}&text={message}&apikey={apikey}'
  response = requests.get(url)
  if response.status_code == 200:
    return 'success'
  else:
    return None
def main():
  while True:
    price, title = check_amazon_price()
    if price <= budget:
      message = f'price alert! {title} is now {price}! buy at: {URL}'
      print(price)
      if send_to_whatsapp(message):
        print('alert send! stopping...')
        break
    else:
      print(f"product is {price}. that's to much. retrying in {time_wait} seconds")
    time.sleep(time_wait)
if __name__ == '__main__':
  main()