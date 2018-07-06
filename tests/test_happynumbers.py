import unittest

from happynumbers import happy


class HappyNumbersTest(unittest.TestCase):
    def test_happy_1(self):
        self.assertEqual(True, happy(1))

    def test_happy_all(self):
        self.assertTrue(all(happy(n) for n in [10, 13, 203, 2003]))

    def test_not_happy_all(self):
        self.assertFalse(all(happy(n) for n in [2, 3, 12, 77, 2004]))