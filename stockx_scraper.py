from itertools import cycle
import requests
from bs4 import BeautifulSoup
import pandas as pd
import random
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


baseurl = 'https://stockx.com'

# multiple user agents

user_agents_list = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)"
    "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)"
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)"
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0;  Trident/5.0)"
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0; MDDCJS)"

]


productlinks = []

# multiple proxies


# list_proxy = [
#     'http://Username:Password@IP1:20000',
#     'http://Username:Password@IP2:20000',
#     'http://Username:Password@IP3:20000',
#     'http://Username:Password@IP4:20000',
# ]

# proxy_cycle = cycle(list_proxy)
# proxy = next(proxy_cycle)

# for i in range(1, 10):
#     proxy = next(proxy_cycle)
#     print(proxy)
#     proxies = {
#         "http": proxy,
#         "https": proxy
#     }
#     k = requests.get('https://stockx.com/sneakers',
#                      headers={'User-Agent': random.choice(user_agents_list)}, timeout=120, proxies=proxies).text
# for i in range(1, 26):

#     k = requests.get('https://stockx.com/sneakers',
#                      headers={'User-Agent': random.choice(user_agents_list)}, timeout=120, proxies=proxies).text

#     soup = BeautifulSoup(k, 'html.parser')

#     productlist = soup.find_all(
#         'div', class_='css-1ibvugw-GridProductTileContainer')

#     print(productlist)
# for item in productlist:
#     for link in item.find_all('a', href=True):
#         productlinks.append(baseurl + link['href'])

# print(productlinks)

shoe_links = ['https://stockx.com/air-jordan-3-retro-white-cement-reimagined', 'https://stockx.com/air-jordan-5-retro-unc-university-blue', 'https://stockx.com/puma-lamelo-ball-mb02-rick-and-morty-adventures', 'https://stockx.com/nike-air-force-1-low-sp-tiffany-and-co', 'https://stockx.com/nike-air-force-1-low-sp-ambush-phantom', 'https://stockx.com/new-balance-1906d-protection-pack-harbor-grey', 'https://stockx.com/nike-dunk-low-retro-white-black-2021', 'https://stockx.com/nike-dunk-low-white-black-2021-w', 'https://stockx.com/nike-dunk-low-retro-white-black-gs', 'https://stockx.com/nike-dunk-low-grey-fog', 'https://stockx.com/air-jordan-6-retro-cool-grey', 'https://stockx.com/air-jordan-13-retro-playoffs-2023', 'https://stockx.com/nike-air-force-1-low-white-07', 'https://stockx.com/adidas-campus-bad-bunny-cream', 'https://stockx.com/air-jordan-1-low-se-concord', 'https://stockx.com/air-jordan-11-retro-cherry-2022', 'https://stockx.com/air-jordan-4-retro-oil-green-w', 'https://stockx.com/nike-dunk-low-valentines-day-2023', 'https://stockx.com/air-jordan-1-mid-space-jam', 'https://stockx.com/air-jordan-4-retro-se-craft-photon-dust',
              'https://stockx.com/air-jordan-1-retro-high-og-true-blue', 'https://stockx.com/nike-dunk-low-rose-whisper-w', 'https://stockx.com/nike-dunk-low-summit-white-midnight-navy', 'https://stockx.com/nike-sb-dunk-low-pro-white-gum', 'https://stockx.com/air-jordan-6-retro-cool-grey-gs-2023', 'https://stockx.com/air-jordan-1-retro-high-85-black-white-2023', 'https://stockx.com/nike-dunk-low-industrial-blue-sashiko', 'https://stockx.com/air-jordan-1-retro-low-og-doernbecher-2023', 'https://stockx.com/nike-sb-dunk-low-pro-iso-orange-label-grey-gum', 'https://stockx.com/nike-dunk-low-light-orewood-brown-sashiko', 'https://stockx.com/adidas-yeezy-slide-bone-2022', 'https://stockx.com/air-jordan-4-retro-white-midnight-navy', 'https://stockx.com/nike-dunk-low-retro-miami-hurricanes', 'https://stockx.com/nike-dunk-low-next-nature-white-black-w', 'https://stockx.com/nike-dunk-low-retro-red-swoosh-panda', 'https://stockx.com/new-balance-550-white-green', 'https://stockx.com/nike-air-force-1-low-supreme-box-logo-white', 'https://stockx.com/air-jordan-5-retro-aqua', 'https://stockx.com/adidas-yeezy-slide-black-onyx', 'https://stockx.com/nike-air-max-1-crepe-soft-grey']

sneakers = {}
for i in shoe_links:

    testlink = i

    r = requests.get(testlink, headers={
        'User-Agent': random.choice(user_agents_list)}, timeout=120)

    soup = BeautifulSoup(r.content, 'lxml')

    name_data = soup.find_all('h1', class_="chakra-heading css-1vj6v5q",
                              attrs={"data-component": "primary-product-title"})

    full_name = ''

    price_data = soup.find('p', class_="chakra-text css-xfmxd4").text

    for i in name_data:
        i = str(i)
        name = i.split('<')
        initial = name[1][77::]
        final = name[-3][81::]
        full_name += initial + ' ' + final

    sneakers[full_name] = price_data
    print(sneakers)
