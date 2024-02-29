#!/usr/bin/python3
"""City model test"""


import unittest
from models.review import Review


class TestReviewModel(unittest.TestCase):
    def setUp(self):
        self.review = Review()
        self.review.place_id = "1"
        self.review.user_id = "1"
        self.review.text = "example test"

    def test_type(self):
        self.assertIsInstance(Review.place_id, str)
        self.assertIsInstance(Review.user_id, str)
        self.assertIsInstance(Review.text, str)

    def test_place_id(self):
        self.assertEqual(self.review.place_id, "1")

    def test_user_id(self):
        self.assertEqual(self.review.user_id, "1")

    def test_text(self):
        self.assertEqual(self.review.text, "example test")
