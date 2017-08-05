import requests
import json
from time import sleep

REFRESH_RATE = input('Enter a refresh rate in milliseconds: ')

while (True):
    API_LINK = 'https://api.coinmarketcap.com/v1/ticker/'
    HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    
    re = requests.Session()
    page = re.get(API_LINK, headers=HEADERS)
    coin_content = json.loads(page.text)
    
    with open('coins.json', 'w') as outfile:
        json.dump(coin_content, outfile, indent=4, sort_keys=True)
        
    collective_info = ''
    
    for coin_info in coin_content:
        collective_info = 'Name: ' + coin_info['name'] + '\n'
        collective_info += 'Rank: ' + str(coin_info['rank']) + '\n'
        collective_info += 'Price in USD: $' + str(coin_info['price_usd']) + '\n'
        collective_info += 'Price in Bitcoins: $' + str(coin_info['price_btc']) + '\n'
        collective_info += 'Symbol: ' + str(coin_info['symbol']) + '\n'
        collective_info += 'Percent change in the last hour: ' + str(coin_info['percent_change_1h']) + '%\n'
        collective_info += 'Percent change in the last 24 hours: ' + str(coin_info['percent_change_24h']) + '%\n'
        collective_info += 'Percent change in the last week: ' + str(coin_info['percent_change_7d']) + '%\n'
        collective_info += 'Total supply of {}: '.format(coin_info['name']) + str(coin_info['total_supply']) + '%\n'
        collective_info += 'Total available supply of {}: '.format(coin_info['name']) + str(coin_info['available_supply']) + '%\n'
        
        print collective_info
        
    re.close()
    sleep(REFRESH_RATE)