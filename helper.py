import feedparser
import re
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_region():
    """
    Returns the craigslist region relevant to user

    First tries to catch redirect of craigslist.org
    if redirect fails, asks user to input manually

    Parameters: None
    Returns string relating to craigslist region
    """
    found = None
    with urllib.request.urlopen('https://craigslist.org/') as response:
        redirect = response.geturl()
        m = re.search('.*\/([a-z]+)\.craigslist\.org', redirect)
        if m:
            found = m.group(1)
        if found == 'www' or None:
            print("Region discovery failed")
            print("Please enter your local region such that")
            found = input(
                '[your region].craigslist.org goes to your local region: ')
    return found

def get_new_listings(region):
    rssfeed = 'https://' + region + '.craigslist.org/search/apa?format=rss'
    parsed = feedparser.parse(rssfeed)
    urls = (parsed['items']) if parsed else []
    return urls

def scrape(link):
    m = re.search('.*\/([a-z]+)\/apa\/d\/([^\/]+)\/(\d+)\.html', url)
    region = m.group(1)
    name = m.group(2)
    id = m.group(3)
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')

    geo = soup.find('meta', {'name':"geo.position"})
    geo = geo["content"] if geo else None

    placename = soup.find('meta', {'name':"geo.placename"})
    placename = placename["content"] if placename else None

    title = soup.find('meta', {'property':"og:title"})
    title = title["content"] if title else None

    image = soup.find('meta', {'property':"og:image"})
    image = image["content"] if image else None

    price = soup.find('span', {'class':"price"})
    price = int(price.get_text(strip=True)[1:]) if price else None

    housing = soup.find('span', {'class':"housing"})
    housing = housing.get_text(strip=True) if housing else None

    bedrooms = None
    sqft = None
    if housing:
        if 'br' in housing:
            b = re.search('.* (\d+)br', housing)
            bedrooms = int(b.group(1))
        if 'ft' in housing:
            f = re.search('.* (\d+)ft', housing)
            sqft = int(f.group(1))

    address = soup.find('div', {'class':'mapaddress'})
    address = address.get_text(strip=True) if address else None

    gmaps = soup.find('p', {'class':'mapaddress'}).find('a')["href"]

    attrgroup = soup.find_all('p', {'class':'attrgroup'})
    attributes = attrgroup[1].get_text(strip=False) if attrgroup else None

    body = soup.find('section', {'id':'postingbody'})
    body = body.get_text(strip=False) if body else None




#def __init__:
#
#

#items = (d['items'])
#print("Found", len(items), "items")
#for item in items:
#    url = item['id']
#
#            post_data = {
#                'id': id,
#                'url': url,
#                'name': name,
#                'region': region,
#                'geo': geo,
#                'placename': placename,
#                'title': title,
#                'image': image,
#                'price': price,
#                'housing': housing,
#                'bedrooms': bedrooms,
#                'sqft': sqft,
#                'address': address,
#                'gmaps': gmaps,
#                'attributes': attributes,
#                'body': body,
#                }
#
#            result = posts.insert_one(post_data)
#            print('One post: {0}'.format(result.inserted_id))
#
#    cursor.close()
#    conn.close()
#except Exception as e:
#    print("Uh oh, can't connect. Invalid dbname, user or password?")
#    print(e)
