# Homescraper
Service for identifying new craigslist listings that are desirable and notifying
 when they become listed.

Grabs the latest housing urls from craigslist rss feed, scrapes data for each
 new listing, and saves it to a local database. When discovering a new listing
 that fits the user parameters it notifies the user.

## Setup:
```
pip install -r requirements.txt
```

## Before running script start Mongdb:
`sudo service mongod start`

## Usage:
For help run `python3 homescraper.py -h`

Input search info as command arguments in the format shown below

Arguments in [] are optional, arguments outside of brackets are mandatory
```
python3 homescraper.py [-h] [--bedrooms] [--spacemin] [--spacemax] [--cats] [--dogs] [--wd]
                      distance geo geo pricemin pricemax
```
example:
`python3 homescraper.py 5 37.557516 -122.287266 2000 3000 --bedrooms 1 --cats`
