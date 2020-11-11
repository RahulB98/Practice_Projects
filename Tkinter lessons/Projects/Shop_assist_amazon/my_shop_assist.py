import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
import ssl
import pandas as pd
import time

def get_price(row, url):
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    lookup_time = time.now().strftime('%Y-%m-%d %Hh%Mm')

    link = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(link, 'html.parser')

    try:
        title = soup.find(id="productTitle").get_text().split()
    except:
        title = None

    try:
        price = soup.find(id="priceblock_dealprice").get_text().split()
    except:
        price = None
    if price == None:
        try:
            price = soup.find(id="priceblock_ourprice").get_text().split()
        except:
            try:
                price = soup.find(id="priceblock_saleprice").get_text().split()
            except:
                price = ''
                print("Cannot find price")
    article_title = " ".join(title)
    article_price = float(price[1].replace(",", ""))
    if article_price <= file.desired_price[row]:
        print("*****BUY NOW: " + article_title + " ************")
    print(article_title, ": ", article_price)

file = pd.read_csv('items_list.csv', sep=',')
urls = file.url
for row, url in enumerate(urls):
    get_price(row, url)