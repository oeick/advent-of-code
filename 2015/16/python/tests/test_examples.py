import unittest

import main


class ExampleTests(unittest.TestCase):

    def test_part_1(self):
        result = main.solve_part_1(
            {'1': ['trees: 7', 'perfumes: 2', 'akitas: 5'],
             '2': ['children: 3', 'goldfish: 4', 'vizslas: 0'],
             '3': ['children: 3', 'goldfish: 5', 'vizslas: 0']}
        )
        self.assertEqual(3, result)

    def test_part_2(self):
        result = main.solve_part_2(
            {'1': ['perfumes: 1', 'trees: 2', 'goldfish: 0'],
             '2': ['perfumes: 1', 'trees: 6', 'goldfish: 5'],
             '3': ['perfumes: 1', 'trees: 6', 'goldfish: 0']}
        )
        self.assertEqual(3, result)
