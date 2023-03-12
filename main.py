import discord
from discord.ext import commands
from discord import app_commands
from datetime import date
from urllib import request
from datetime import date, datetime
from bs4 import BeautifulSoup as bs
import re

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

async def notify(ctx: discord.Interaction):
    url = request.urlopen('https://www.nike.com/in/launch').read()
    s = bs(url, 'lxml')
    figs = s.find_all('figures')
    links = s.find_all('a', attrs={'data-qa': 'product-card-link'})
    sneaker_links = []
    for i in links:
        if i.get('href').startswith('/'):
            sneaker_links.append(i.get('href'))
    latest = sneaker_links[0]
    tmp = 'https://www.nike.com' + latest
    prod_url = request.urlopen(tmp)
    p = bs(prod_url, 'lxml')
    latest_snkr_name = p.find('h1', class_='headline-5=small').text + ' ' + p.find('h5', class_='headline-2').text
    latest_snkr_price = p.find('p', class_='adaptive-price').text
    print(f'{latest_snkr_name} is currently available for {latest_snkr_price}')
    


bot.run('MTA4MzAyNzI5Nzg2ODcyNjM3Mw.GTU-mR.AAGEpTwgtqlVnoVLzGmXGbEbSPSLF9P6afhHnU')