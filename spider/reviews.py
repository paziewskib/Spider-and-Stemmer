import requests
import re
from bs4 import BeautifulSoup
import sys
import xml.etree.ElementTree as ET
import urllib2
import lxml

reload(sys)
sys.setdefaultencoding('utf8')


def trade_spider():
    page = 1
    plik = open('1128_wynik_reviews.txt', 'w')
    id_zdania = 0
    while page < 2:
        url = 'https://www.zzounds.com/sitemap_product_reviews.xml'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('loc'):
            id_zdania+=1
            url = link.string
            plik.write(get_single_item_data(url))
        page += 1
    plik.close()

def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    dane = ""
    for item_name in soup.findAll('span', {'class': "span-30 last clear append-bottom user-review-txt"}):
        dane += item_name.text
    print dane
    return dane


trade_spider()

