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
        # Find most recent listings
        self.urls = helper.get_new_listings(self.region)
        for url in self.urls:
            region, name, id = helper.parse_url(url)
            if dbhelper.not_in(id, self.posts):
                content = helper.scrape(url)
                # Skip listing if page has been removed by user
                if content['placename'] == None:
                    continue
                content.update(
                    {'region': region,
                     'name': name,
                     'id': id,
                     'url': url,
                     })
                score = matcher.calculate_score(content, self.target)
                content.update({'score': score})
                dbhelper.post(content, self.posts)
                if matcher.matches_search(content, self.target):
                    print("Found one listing that matches!")
                    print("score:", content['score'], content['url'])
                    score_rank =  dbhelper.score_rank(id, self.posts)
                    if score_rank <= 20:
                        print("TOP 20")
                        # Notify user

    def print_top(self, n):
        dbhelper.print_top(n, self.posts)

search = Homescraper()
search.scrape_latest_results()
search.print_top(10)
