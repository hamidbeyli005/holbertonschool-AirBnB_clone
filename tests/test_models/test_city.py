#!/usr/bin/python3
"""City model test"""


import unittest
from models.city import City


class TestCityModel(unittest.TestCase):
	def setUp(self):
		self.city = City()
		self.city.state_id = "1"
		self.city.name = "Baku"
	
	def test_id(self):
		self.assertEqual(self.city.state_id, "1")

	def test_name(self):
		self.assertEqual(self.city.name, "Baku")
