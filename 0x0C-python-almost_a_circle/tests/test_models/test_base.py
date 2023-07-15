import unittest
from models.base import Base


class BaseTestCase(unittest.TestCase):
    def test_base_id_increment(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_base_id_increment_multiple(self):
        b2 = Base()
        b3 = Base()
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_base_id_with_parameter(self):
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)


if __name__ == '__main__':
    unittest.main()
