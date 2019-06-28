# Python code to demonstrate working of unittest
import unittest
import helper
import validators


class HelperTests(unittest.TestCase):

	def setUp(self):
		self.region = helper.get_region()
		self.urls = helper.get_new_listings(self.region)
		self.post_data = helper.scrape(self.urls[0])
		pass

	# Returns True if the string contains 4 a.
	def test_get_region_string(self):
		self.assertTrue(isinstance(self.region, str))

	def test_get_region_not_www(self):
		self.assertFalse(self.region == 'www')

	def test_get_new_listings_list(self):
		self.assertTrue(isinstance(self.urls, list))

	def test_get_new_listings_contains_urls(self):
		self.assertTrue(validators.url(self.urls[0]))

	# Returns True if the string is in upper case.
	#def test_distance(self):
	#	self.assertEqual(type(self.iotest.distance), type(1))
#
	#def test_geo(self):
	#	self.assertEqual(type(self.iotest.geo), type([]))
#
	#def test_geox(self):
	#	self.assertEqual(type(self.iotest.geo[0]), type(1.0))
#
	#def test_geoy(self):
	#	self.assertEqual(type(self.iotest.geo[1]), type(1.0))
#
	#def test_pricemin(self):
	#	self.assertEqual(type(self.iotest.pricemin), type(1))
#
	#def test_pricemax(self):
	#	self.assertEqual(type(self.iotest.pricemax), type(1))

if __name__ == '__main__':
	unittest.main()
