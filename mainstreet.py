# from itertools import cycle
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import random
# from requests.adapters import HTTPAdapter
# from urllib3.util.retry import Retry


# baseurl = 'https://marketplace.mainstreet.co.in/'

# # multiple user agents

# user_agents_list = [
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0",
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"
#     "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)"
#     "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)"
#     "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)"
#     "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0;  Trident/5.0)"
#     "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0; MDDCJS)"

# ]

# k = requests.get('https://marketplace.mainstreet.co.in/collections/sneakers/')

# soup = BeautifulSoup(k.content, 'html.parser')


# productlist = soup.find_all(
#     'div', {'class': 'spf-product__info'})

# print(productlist)
from requests_html import HTMLSession
from dump import mainstreet

s = HTMLSession()

def get_stuff(url):
    r = s.get(url)
    r.html.render(sleep=1, timeout=20)

    print(r.html)
    # price = r.html.xpath('''/html/body/div[2]/div[3]/div[1]/div[2]/div[2]/div[1]/p[4]/span''', first=True).text
    # sizes = r.html.xpath('''/html/body/div[2]/div[3]/div[1]/div[2]/div[2]/div[1]/form/div[3]/div/div[1]/div/ul/li''') 
    
    # print(sizes) 
get_stuff('https://www.vegnonveg.com/products/w-blazer-low-77-jumbo-whitemalachite-university-blue')


# for i in mainstreet:
#     try:
#         info = get_stuff('https://marketplace.mainstreet.co.in' + i)
#         print('name-', info[0])
#         print('price-', info[1])
#         print(info[3])
#     except Exception as e:
#         print(i, e)

