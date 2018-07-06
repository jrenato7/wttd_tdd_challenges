import unittest

from fizzbuzz import fizzbuzz


class FizzBuzzTest(unittest.TestCase):
    def test_responde_fizz_para_3(self):
        self.assertEqual('fizz', fizzbuzz(3))

    def test_responde_fizz_para_6(self):
        self.assertEqual('fizz', fizzbuzz(6))

    def test_responde_fizz_para_9(self):
        self.assertEqual('fizz', fizzbuzz(9))

    def test_responde_buzz_para_5(self):
        self.assertEqual('buzz', fizzbuzz(5))

    def test_responde_buzz_para_10(self):
        self.assertEqual('buzz', fizzbuzz(10))

    def test_responde_buzz_para_20(self):
        self.assertEqual('buzz', fizzbuzz(20))

    def test_responde_fizzbuzz_para_15(self):
        self.assertEqual('fizzbuzz', fizzbuzz(15))

    def test_responde_fizzbuzz_para_30(self):
        self.assertEqual('fizzbuzz', fizzbuzz(30))

    def test_responde_fizzbuzz_para_45(self):
        self.assertEqual('fizzbuzz', fizzbuzz(45))

    def test_responde_1_para_1(self):
        self.assertEqual('1', fizzbuzz(1))

    def test_responde_2_para_2(self):
        self.assertEqual('2', fizzbuzz(2))

    def test_responde_4_para_4(self):
        self.assertEqual('4', fizzbuzz(4))
