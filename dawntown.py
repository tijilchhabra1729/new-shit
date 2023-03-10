from itertools import cycle
import requests
from bs4 import BeautifulSoup
import pandas as pd
import random
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


baseurl = 'https://dawntown.in'
productlinks = []

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

k = requests.get('https://dawntown.in/collections/dunk',
                 headers={'User-Agent': random.choice(user_agents_list)}, timeout=120).text

soup = BeautifulSoup(k, 'html.parser')

productlist = soup.find_all(
    'div', class_='card-information__wrapper')

for item in productlist:
    for link in item.find_all('a', href=True):
        productlinks.append(baseurl + link['href'])


print(productlinks)
