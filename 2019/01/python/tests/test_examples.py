import unittest
import main

from parameterized import parameterized


class ExampleTests(unittest.TestCase):

    @parameterized.expand([
        (2, 12),
        (2, 14),
        (654, 1969),
        (33583, 100756)])
    def test_part_1_examples(self, expected: int, mass: int):
        self.assertEqual(expected, main.solve_part_1([mass]))

    @parameterized.expand([
        (2, 14),
        (966, 1969),
        (50346, 100756)])
    def test_part_2_examples(self, expected: int, mass: int):
        self.assertEqual(expected, main.solve_part_2([mass]))
