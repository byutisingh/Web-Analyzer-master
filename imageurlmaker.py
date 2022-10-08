from bs4 import BeautifulSoup as bs
import requests
from urllib.request import urlparse, urljoin
import getlinks as gl
href="abc.jpg"
siteurl=gl.getDomainName("http://varanasikshetra.com/abc.jpg")
s="<img src=\"http://varanasikshetra.com/abc.jpg\"/>"
scraper = bs(s, 'html.parser')
h1s=scraper.find_all("img")
#print(h1s[0].get('src'))
print("URL is ",siteurl)
siteurl="http://" + siteurl
href = urljoin(siteurl, href)
print("HREF",href)
