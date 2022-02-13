import unittest

import main


class ExampleTests(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(
            18,
            main.solve_part_1([[5, 1, 9, 5],
                               [7, 5, 3],
                               [2, 4, 6, 8]]))

    def test_part_2(self):
        self.assertEqual(
            9,
            main.solve_part_2([[5, 9, 2, 8],
                               [9, 4, 7, 3],
                               [3, 8, 6, 5]]))
