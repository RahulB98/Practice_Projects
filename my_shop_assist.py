import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter - ')

link = urllib.request.urlopen(url).read()
soup = BeautifulSoup(link, 'html.parser')

tags = soup('td')
for tag in tags:
    if tag.get('class') == ['a-span12']:
        print(tag)
