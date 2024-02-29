#!/usr/bin/python3
"""Place model test"""


import unittest
from models.place import Place


class TestPlaceModel(unittest.TestCase):
	def setUp(self):
		self.place = Place()
		self.place.city_id = "1"
		self.place.user_id = "1"
		self.place.name = "Good Hotel"
		self.place.description = "Very good place"
		self.place.number_rooms = 3
		self.place.number_bathrooms = 2
		self.place.max_guest = 6
		self.place.price_by_night = 99
		self.place.latitude = 74.16
		self.place.longitude = 68.92
		self.place.amenity_ids = []
	
	def test_city_id(self):
		self.assertEqual(self.place.city_id, "1")

	def test_user_id(self):
		self.assertEqual(self.place.user_id, "1")

	def test_name(self):
		self.assertEqual(self.place.name, "Good Hotel")
	
	def test_description(self):
		self.assertEqual(self.place.description, "Very good place")

	def test_number_rooms(self):
		self.assertEqual(self.place.number_rooms, 3)

	def test_number_bathrooms(self):
		self.assertEqual(self.place.number_bathrooms, 2)

	def test_max_guest(self):
		self.assertEqual(self.place.max_guest, 6)

	def test_price(self):
		self.assertEqual(self.place.price_by_night, 99)

	def test_latitude(self):
		self.assertEqual(self.place.latitude, 74.16)

	def test_longitude(self):
		self.assertEqual(self.place.longitude, 68.92)

	def test_amenity_ids(self):
		self.assertEqual(self.place.amenity_ids, [])
