#!/usr/bin/python3
"""Amenity model test"""


import unittest
from models.amenity import Amenity


class TestAmenityModel(unittest.TestCase):
	def setUp(self):
		self.amenity = Amenity()
		self.amenity.name = "Good"
	def test_name(self):
		self.assertEqual(self.amenity.name, "Good")
