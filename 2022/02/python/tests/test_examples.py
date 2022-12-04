import unittest

import main

EXAMPLE = [
    'A Y',
    'B X',
    'C Z']


class ExampleTests(unittest.TestCase):

    def test_example_part_1(self):
        self.assertEqual(15, main.solve_part_1(EXAMPLE))

    def test_example_part_2(self):
        self.assertEqual(12, main.solve_part_2(EXAMPLE))
