import unittest

import main

EXAMPLE = [
    'vJrwpWtwJgWrhcsFMMfFFhFp',
    'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
    'PmmdzqPrVvPwwTWBwg',
    'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
    'ttgJtRGJQctTZtZT',
    'CrZsJsPPZsGzwwsLwLmpwMDw']


class ExampleTests(unittest.TestCase):

    def test_example_part_1(self):
        self.assertEqual(157, main.solve_part_1(EXAMPLE))

    def test_example_part_2(self):
        self.assertEqual(70, main.solve_part_2(EXAMPLE))
