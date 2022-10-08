from urllib.request import urljoin
from bs4 import BeautifulSoup as bs
import getlinks as gl


from bs4 import BeautifulSoup as bs

import getlinks as gl


def GetDivs(html):
    scraper = bs(html, 'html.parser')
    divs = scraper.find_all("div")
    divisions = {}
    n = 0
    for div in divs:
        divisions[n] = divs[n]
        n = n + 1
    return divisions


def GetHeadings(html):
    scraper = bs(html, 'html.parser')
    h1s = scraper.find_all("h2")
    headings = {}
    n = 0
    for h1 in h1s:
        headings[n] = h1s[n]
        n = n + 1
    return headings


def GetParagraphs(html):
    scraper = bs(html, 'html.parser')
    h1s = scraper.find_all("p")
    headings = {}
    n = 0
    for h1 in h1s:
        headings[n] = h1s[n]
        n = n + 1
    return headings


def GetImages(html, siteurl):
    siteurl = gl.getDomainName(siteurl)
    siteurl = "http://" + siteurl
    scraper = bs(html, 'html.parser')
    h1s = scraper.find_all("img")
    headings = {}
    n = 0

    for h1 in h1s:
        src = h1s[n].get('src')
        alt = h1s[n].get('alt')
        newurl = urljoin(siteurl, src)
        # print(newurl)
        # data="<img src='" + newurl + "'/>"
        d = {}
        d["src"] = newurl
        d["alt"] = alt
        # h1s[n].set('src',data)
        headings[n] = d
        # headings[n]=data
        n = n + 1
    return headings


def GetImagesAlt(html):
    scraper = bs(html, 'html.parser')
    h1s = scraper.find_all("img")
    headings = {}
    n = 0

    for h1 in h1s:
        alt = h1s[n].get('alt')

        headings[n] = alt
        n = n + 1
    return headings

# scraper.title.string
#    scraper.div.s````````tring
