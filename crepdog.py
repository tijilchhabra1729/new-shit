from itertools import cycle
import requests
from bs4 import BeautifulSoup
import pandas as pd
import random
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import time
from selenium import webdriver


baseurl = 'https://crepdogcrew.com'
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

##### Web scrapper for infinite scrolling page #####
driver = webdriver.Chrome()
driver.get("https://crepdogcrew.com/collections/all-dunks")
time.sleep(2)  # Allow 2 seconds for the web page to open
# You can set your own pause time. My laptop is a bit slow so I use 1 sec
scroll_pause_time = 5
screen_height = driver.execute_script(
    "return window.screen.height;")   # get the screen height of the web
i = 1

while True:
    # scroll one screen height each time
    driver.execute_script(
        "window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
    i += 1
    time.sleep(scroll_pause_time)
    # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
    scroll_height = driver.execute_script("return document.body.scrollHeight;")
    # Break the loop when the height we need to scroll to is larger than the total scroll height
    if (screen_height) * i > scroll_height:
        break


k = requests.get('https://crepdogcrew.com/collections/all-dunks',
                 headers={'User-Agent': random.choice(user_agents_list)}, timeout=120).text

soup = BeautifulSoup(k, 'html.parser')

productlist = soup.find_all(
    'h2', class_='ProductItem__Title Heading')

for item in productlist:
    for link in item.find_all('a', href=True):
        productlinks.append(baseurl + link['href'])


print(productlinks)
