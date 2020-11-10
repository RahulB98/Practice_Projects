import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
import ssl
import csv
import pandas as pd

def get_price(url, desired_price):
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

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
    if article_price <= desired_price:
        print("*****BUY NOW: " + article_title + " ************")
    print(article_title, ": ", article_price)
'''
link_1 = ['https://www.amazon.in/gp/product/B07XVMDRZY/ref=s9_acss_bw_cg_Headers_2d1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-12&pf_rd_r=16PQHT6J2KFZW359EV9D&pf_rd_t=101&pf_rd_p=00cb27c4-faf9-47e8-8899-c96f8fbb7ef8&pf_rd_i=1389401031', 50000]
link_2 = ['https://www.amazon.in/dp/B012TRTE6M/ref=twister_dp_update?_encoding=UTF8&psc=1', 1500]
link_3 = ['https://www.amazon.in/ASUS-FX505DT-15-6-inch-Graphics-FX505DT-BQ151T/dp/B08CY2M684', 51000]
url_list = [link_1, link_2, link_3]
'''
file = pd.read_csv()
        #for url, desired_price in url_list:
        #  get_price(url, desired_price)