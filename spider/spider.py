import requests
from bs4 import BeautifulSoup
import sys
import xml.etree.ElementTree as ET
reload(sys)
sys.setdefaultencoding('utf8')


def trade_spider():
    page = 1
    plik = open('1128_wynik_guitar_second.txt', 'w')
    id_zdania = 0
    while page < 2:
        url = 'https://www.zzounds.com/sitemap_product_guitar.xml'
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
    for item_name in soup.findAll('h1', {'id': 'product-title'}):
        dane += item_name.string
    dane += "\n"
    print dane
    return dane


trade_spider()