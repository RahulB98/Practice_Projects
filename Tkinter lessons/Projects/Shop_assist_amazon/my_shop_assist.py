import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
import ssl
import pandas as pd
import time
import csv

def get_price():
    file = pd.read_csv('items_list.csv', sep=',')
    urls = file.url
    for row, url in enumerate(urls):
        # Ignore SSL certificate errors
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        lookup_time = time.strftime('%Y-%m-%d %Hh%Mm')

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
                    price = None
        article_title = " ".join(title)
        if price != None:
            article_price = float(price[1].replace(",", ""))
            if article_price <= file.desired_price[row]:
                alert_message = "*****BUY NOW: " + article_title + " ************"
                print(alert_message)
            else:
                alert_message = "NA"
            print(article_title, ": ", article_price)
            with open("search_results.csv", 'a', newline='') as f:
                w = csv.writer(f, dialect='excel')
                result = [article_title, str(article_price), str(lookup_time), alert_message]
                w.writerow(result)
        else:
            print("Price of this article was not found")
            with open("search_results.csv", 'a', newline='') as f:
                w = csv.writer(f, dialect='excel')
                w.writerow([article_title, 'NA', str(lookup_time), "item price not found!"])
                
get_price()
