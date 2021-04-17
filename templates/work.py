import numpy as np
from Crypto.PublicKey import RSA
import json
from flask import Flask
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import os
import requests
import pandas as pd
from pprint import pprint

app = Flask(__name__)



url_times = 'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml'
url_ny_daily_news = 'https://www.nydailynews.com/arcio/rss/category/news/?sort=display_date:desc'
url_cbs_boston = 'https://boston.cbslocal.com/feed/'
url_cbs_tampa = 'https://tampa.cbslocal.com/feed/'

news = []

for url in [url_times, url_ny_daily_news, url_cbs_boston, url_cbs_tampa]:
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, features='xml')
    items = soup.findAll('item')
    if url == url_times:
        news_outlet = 'ny_times'
    elif url == url_ny_daily_news:
        news_outlet = 'ny_daily_news'
    elif url == url_cbs_boston:
        news_outlet = 'cbs_boston'
    elif url == url_cbs_tampa:
        news_outlet = 'cbs_tampa'

    news_items = []
    for item in items:
        news_item = {}
        news_item['News_Outlet'] = news_outlet
        news_item['title'] = item.title.text
        news_item['description'] = item.description.text
        news_item['link'] = item.link.text
        news_item['pubDate'] = item.pubDate.text
        news_items.append(news_item)
    news.append(news_items)

for item in news:
    print(len(item))

if __name__ == '__main__':
    app.run(debug=True)

