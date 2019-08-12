from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
counts = dict()

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    tagss = tag.split()
    counts[tagss] = counts.get(tagss,0) + 1

list = list()

for key,value in counts.items() :
	list.append((key,value))
list.sort()

for position, count in list :

    print(position, count)
