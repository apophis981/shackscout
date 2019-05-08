import feedparser
from pymongo import MongoClient
import pprint
import re

client = MongoClient()

db = client.test_database
posts = db.posts

d = feedparser.parse('https://sfbay.craigslist.org/search/apa?format=rss')
items = (d['items'])
for item in items:
    url = item['id']
    m = re.search('.*\/([a-z]+)\/apa\/d\/([^\/]+)\/(\d+)\.html', url)
    region = m.group(1)
    name = m.group(2)
    id = m.group(3)
    print(region)
    print(name)
    print(id)
    #post_id = posts.insert_one(post).inserted_id
#pprint.pprint(posts.find_one())
