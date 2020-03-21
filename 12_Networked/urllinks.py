# The program prompts for a web address, then opens the web page, reads the data and passes
# the data to the BeautifulSoup parser, and then retrieves all of the anchor tags and prints
# out the href attribute for each tag.

# Enter - https://docs.python.org (직접 타이핑 해서 넣을 것 !)

import urllib.arequest, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')   # https://docs.python.org (직접 타이핑 해서 넣을 것 !)
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))

