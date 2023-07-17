#!/usr/bin/python3
""" test rectangle """
import unittest
from models.rectangle import Rectangle


class RectangleTestCase(unittest.TestCase):
    """ test """

    def test_Rectangle_id_increment(self):
        b1 = Rectangle()
        self.assertEqual(b1.id, 1)

    def test_Rectangle_id_increment_multiple(self):
        b2 = Rectangle()
        b3 = Rectangle()
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_Rectangle_id_with_parameter(self):
        b4 = Rectangle(12)
        b5 = Rectangle()
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)


if __name__ == '__main__':
    unittest.main()
