from helpers import helper, iohandler, dbhelper, matcher
import sys
from pymongo import MongoClient

class Homescraper:
    def __init__(self):

        # Setup local database instance
        self.client = MongoClient()
        self.db = self.client.homescraper
        self.posts = self.db.posts

        # Get user search specifics
        self.target = iohandler.get_input(sys.argv[1:])

        # Determine local craislist region
        self.region = helper.get_region()

        # Find most recent listings
        self.urls = helper.get_new_listings(self.region)

    def scrape_latest_results(self):
        """
        Main execution of homescraper

        From the latest rss feed of apartment litsings in local craigslist
        for each of the apartment listings first check if that listing is
        already saved in local database. If not add it to local database, check
        if it matches search parameters and notify user if it does

        Parameters: None
        Returns nothing
        """
        for url in self.urls:
            region, name, id = helper.parse_url(url)
            if dbhelper.not_in(id, self.posts):
                content = helper.scrape(url)
                content.update(
                    {'region': region,
                     'name': name,
                     'id': id,
                     'url': url,
                     })
                dbhelper.post(content, self.posts)
                if matcher.matches_search(content, self.target):
                    print("Found one listing that matches!")
                    print(content['url'])
                # Check if it is a matching listing
                    # Notify user

search = Homescraper()
search.scrape_latest_results()
