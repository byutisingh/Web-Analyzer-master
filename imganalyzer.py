from urllib.request import urljoin
from bs4 import BeautifulSoup as bs

html="""
<img src="abc.jpg" alt="Hello"/>
<img src="xyz.jpg" alt="Hi"/>
<img src="http://site.com/abc.jpg" alt="Hello"/>
<a href="http://site.com"/>
<a href="http://site.com/hello"/>
<a href="/hi"/>
<a href="hi"/>




"""


scraper = bs(html, 'html.parser')
urls=scraper.find_all("img")
src=[]
alt=[]
fullurl=[]
siteurl="http://site.com"
l=[]
for url in urls:
    l=l + [url]
    imgsrc=url.get("src")
    newurl = urljoin(siteurl, imgsrc)
    fullurl=fullurl + [newurl]
    src=src + [imgsrc]
#print(l)
print(src)
print(fullurl)

urls=scraper.find_all("a")
print(urls)
fullurl=[]
for url in urls:
    l=l + [url]
    href=url.get("href")
    newurl = urljoin(siteurl, href)
    fullurl=fullurl + [newurl]
print(fullurl)