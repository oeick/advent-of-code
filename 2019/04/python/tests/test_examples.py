import unittest
import main
from parameterized import parameterized


class ExampleTests(unittest.TestCase):

    @parameterized.expand([
        (True, '111111'),
        (False, '223450'),
        (False, '123789')])
    def test_examples_for_part_1(self, expected, pw):
        self.assertEqual(expected, main.solve([pw])[0])

    @parameterized.expand([
        (True, '112233'),
        (False, '123444'),
        (True, '111122')])
    def test_examples_for_part_2(self, expected, pw):
        self.assertEqual(expected, main.solve([pw])[1])
