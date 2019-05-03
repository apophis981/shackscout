import feedparser
import json

d = feedparser.parse('https://sfbay.craigslist.org/search/apa?format=rss')
items = (d['items'])
urls  = set()
for item in items:
    urls.add(item['id'])
print(urls)
