import feedparser
from pymongo import MongoClient
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup


client = MongoClient()

db = client.homescraper
posts = db.posts

d = feedparser.parse('https://sfbay.craigslist.org/search/apa?format=rss')
items = (d['items'])
print("Found", len(items), "items")
for item in items:
    url = item['id']
    m = re.search('.*\/([a-z]+)\/apa\/d\/([^\/]+)\/(\d+)\.html', url)
    region = m.group(1)
    name = m.group(2)
    id = m.group(3)
    exists = posts.find_one({'id': id})
    if not exists:
        print(url)
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

        post_data = {
            'id': id,
            'url': url,
            'name': name,
            'region': region,
            'geo': geo,
            'placename': placename,
            'title': title,
            'image': image,
            'price': price,
            'housing': housing,
            'bedrooms': bedrooms,
            'sqft': sqft,
            'address': address,
            'gmaps': gmaps,
            'attributes': attributes,
            'body': body,
            }

        result = posts.insert_one(post_data)
        print('One post: {0}'.format(result.inserted_id))
