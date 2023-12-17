from unittest import TestCase

from store.logic import operations


class LogicTestCase(TestCase):
    def test_plus(self):
        res = operations(6 ,13, '+')
        self.assertEqual(19, res)

    def test_minus(self):
        res = operations(6 ,13, '-')
        self.assertEqual(-7, res)

    def test_multiply(self):
        res = operations(6, 13, '*')
        self.assertEqual(78, res)
