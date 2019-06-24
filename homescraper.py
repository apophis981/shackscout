import feedparser
import re
from urllib.request import urlopen
import urllib.request
from bs4 import BeautifulSoup
import helper
import iohandler


#get user info
#read cragslist rss feed
#for each result
#if it is not in database
#scrape each page
#save result to database
#if score is in the top 20
#send email
#send text

#target = GetInput()
class Homescraper:
    def __init__(self):
        self.target = iohandler.get_input()
        self.region = helper.get_region()
        self.urls = helper.get_new_listings(self.region)
        for url in self.urls:
            content = helper.scrape(url)
            print(content)
        #    if dbhelper.not_in(content["id"]):
        #        dbhelper.save_to_db(content)
        #        if dbhelper.check_rank(content['id']) <= 20:
        #            # Notify user
        #            print("Found one!")
        #            print(content)


test = Homescraper()


#def __init__:
#
#    d = feedparser.parse(SEARCH_LOCATION)
#    locations = (d['items'])
#    for location in locations:
#

#items = (d['items'])
#print("Found", len(items), "items")
#for item in items:
#    url = item['id']
#    m = re.search('.*\/([a-z]+)\/apa\/d\/([^\/]+)\/(\d+)\.html', url)
#    region = m.group(1)
#    name = m.group(2)
#    id = m.group(3)
#    # Connect to database
#    try:
#        connect_str = "dbname='homescraper' user='apophis' host='localhost' " + \
#        "password='homescraper'"
#        conn = psycopg2.connect(connect_str)
#        cursor = conn.cursor()
#        cursor.execute("SELECT * from homescraper WHERE id = '%s'", (id) )
#        conn.commit() # <--- makes sure the change is shown in the database
#        rows = cursor.fetchall()
#        print(rows)
#        exists = posts.find_one({'id': id})
#        if not exists:
#            print(url)
#            page = urlopen(url)
#            soup = BeautifulSoup(page, 'html.parser')
#
#            geo = soup.find('meta', {'name':"geo.position"})
#            geo = geo["content"] if geo else None
#
#            placename = soup.find('meta', {'name':"geo.placename"})
#            placename = placename["content"] if placename else None
#
#            title = soup.find('meta', {'property':"og:title"})
#            title = title["content"] if title else None
#
#            image = soup.find('meta', {'property':"og:image"})
#            image = image["content"] if image else None
#
#            price = soup.find('span', {'class':"price"})
#            price = int(price.get_text(strip=True)[1:]) if price else None
#
#            housing = soup.find('span', {'class':"housing"})
#            housing = housing.get_text(strip=True) if housing else None
#
#            bedrooms = None
#            sqft = None
#            if housing:
#                if 'br' in housing:
#                    b = re.search('.* (\d+)br', housing)
#                    bedrooms = int(b.group(1))
#                if 'ft' in housing:
#                    f = re.search('.* (\d+)ft', housing)
#                    sqft = int(f.group(1))
#
#            address = soup.find('div', {'class':'mapaddress'})
#            address = address.get_text(strip=True) if address else None
#
#            gmaps = soup.find('p', {'class':'mapaddress'}).find('a')["href"]
#
#            attrgroup = soup.find_all('p', {'class':'attrgroup'})
#            attributes = attrgroup[1].get_text(strip=False) if attrgroup else None
#
#            body = soup.find('section', {'id':'postingbody'})
#            body = body.get_text(strip=False) if body else None
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
