# Python code to demonstrate working of unittest
import unittest
import helper
import validators


class HelperTests(unittest.TestCase):

	def setUp(self):
		self.region = helper.get_region()
		self.urls = helper.get_new_listings(self.region)
		#self.post_data = helper.scrape(self.urls[0])
		pass

	def test_get_region_string(self):
		self.assertTrue(isinstance(self.region, str))

	def test_get_region_not_www(self):
		self.assertFalse(self.region == 'www')

	def test_get_new_listings_list(self):
		print(self.urls)
		self.assertTrue(isinstance(self.urls, list))

	#def test_get_new_listings_contains_urls(self):
	#	self.assertTrue(validators.url(self.urls[0]))

if __name__ == '__main__':
	unittest.main()
