import unittest

from fizzbuzz import fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    def test_responde_fizz(self):
        self.assertEqual('fizz', fizzbuzz(3))
        self.assertEqual('fizz', fizzbuzz(6))
        self.assertEqual('fizz', fizzbuzz(9))

    def test_responde_buzz(self):
        self.assertEqual('buzz', fizzbuzz(5))
        self.assertEqual('buzz', fizzbuzz(10))
        self.assertEqual('buzz', fizzbuzz(20))

    def test_responde_fizzbuzz(self):
        self.assertEqual('fizzbuzz', fizzbuzz(15))
        self.assertEqual('fizzbuzz', fizzbuzz(30))
        self.assertEqual('fizzbuzz', fizzbuzz(45))

    def test_responde_numero(self):
        self.assertEqual('1', fizzbuzz(1))
        self.assertEqual('2', fizzbuzz(2))
        self.assertEqual('4', fizzbuzz(4))