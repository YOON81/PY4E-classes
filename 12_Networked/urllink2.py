# BeautifulSoup to pull out various parts of each tag
# Enter - http://www.dr-chuck.com/page1.htm (주소는 직접 타이핑 할 것!)
# https://github.com/csev/py4e/commit/1aecb3c0a1895fd821b85c585e9d5049086629da


from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')  # ttp://www.dr-chuck.com/page1.htm (주소는 직접 타이핑 할 것!)
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)