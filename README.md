# Apartment and House webcrawler with a smarter search
Grabs the latest housing urls from craigslist rss feed, scrapes data for each
listing, and saves it to a local database

# Setup:
```
pip install BeautifulSoup4
sudo apt-get install -y mongodb-org
pip install feedparser
```

# Before running script start Mongdb:
`sudo service mongod start`

# Usage:
`python3 craigsrss.py`

## Depricated zillow scraper usage
`python3 zillow_scraper.py [zip code] [price_min] [price_max] [hometype]``
