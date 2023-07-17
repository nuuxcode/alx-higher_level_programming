#!/usr/bin/python3
""" test rectangle """
import unittest
from models.square import Square


class SquareTestCase(unittest.TestCase):
    """ test """

    def test_Square_id_increment(self):
        b1 = Square()
        self.assertEqual(b1.id, 1)

    def test_Square_id_increment_multiple(self):
        b2 = Square()
        b3 = Square()
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_Square_id_with_parameter(self):
        b4 = Square(12)
        b5 = Square()
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)


if __name__ == '__main__':
    unittest.main()
