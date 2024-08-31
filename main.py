#kena run kat shell pip install beautifulsoup4
#kena run kat shell pip install requests
from bs4 import BeautifulSoup 
import requests

def get_currency(in_currency, out_currency) :
  url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
  #nak print url kat console
   # print (url) 
    #nak print source code of the website
    #content = requests.get(url).text
    #print(content)
  #use soup
  content = requests.get(url).text
  soup = BeautifulSoup(content, 'html.parser')
  rate = soup.find('span', class_='ccOutputRslt').get_text()
  rate_without4stringback = rate[0:-4]
  
 #print(rate)
 #print(rate_without4stringback)

  return rate_without4stringback


current_rate = get_currency('EUR', 'AUD')
print (current_rate)


