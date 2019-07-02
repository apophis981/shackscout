# Python code to demonstrate working of unittest
import unittest
from helpers import iohandler
import argparse

class IOhandlerTests(unittest.TestCase):

	def setUp(self):
		self.iotest = iohandler.get_input(
			['5', '37.557516', '-122.287266', '2000', '3000', '--bedrooms', '1',
			 '--cats'])
		pass

	# Returns True if the string contains 4 a.
	def test_output_type(self):
		parser = argparse.ArgumentParser(description='Get user search specifics')
		parser.add_argument('distance', type=int)
		nargparse = parser.parse_args(['5'])
		self.assertEqual(type(self.iotest), type(nargparse))

	# Returns True if the string is in upper case.
	def test_distance(self):
		self.assertTrue(isinstance(self.iotest.distance, int))

	def test_geo(self):
		self.assertTrue(isinstance(self.iotest.geo, list))

	def test_geox(self):
		self.assertTrue(isinstance(self.iotest.geo[0], float))

	def test_geoy(self):
		self.assertTrue(isinstance(self.iotest.geo[1], float))

	def test_pricemin(self):
		self.assertTrue(isinstance(self.iotest.pricemin, int))

	def test_pricemax(self):
		self.assertTrue(isinstance(self.iotest.pricemax, int))

if __name__ == '__main__':
	unittest.main()
