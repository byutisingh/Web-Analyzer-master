
import requests
from urllib.request import urlparse, urljoin
from bs4 import BeautifulSoup

# initialize the set of links (unique links)
internal_urls = set()
external_urls = set()

total_urls_visited = 0


def getHref(url):
    return url.get('href')


def is_valid(url):
    """
    Checks whether `url` is a valid URL.
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)
def getDomainName(url):
    #Get the domain name from an url
   return urlparse(url).netloc

def get_all_website_links(url):
   #Find all URLs
    urls = set()
    # domain name of the URL without the protocol
    domain_name = getDomainName(url)
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    
    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        if href == "" or href is None:
           
            continue
        # join the URL if it's relative (not absolute link)
        href = urljoin(url, href)
        parsed_href = urlparse(href) # URL fragments, etc.
        # remove URL GET parameters,
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
        if not is_valid(href):
            # not a valid URL
            continue
        if href in internal_urls:
            # already in the set
            continue
        if domain_name not in href:
            # external link
            if href not in external_urls:
               
                external_urls.add(href)
            continue
       
        urls.add(href)
        internal_urls.add(href)
    return urls,internal_urls,external_urls


def crawl(url, max_urls=50):
   
    global total_urls_visited
    total_urls_visited += 1
    links = get_all_website_links(url)
    for link in links:
        if total_urls_visited > max_urls:
            break
        crawl(link, max_urls=max_urls)


#print(d1)
#print(d2)
#print(d3)
