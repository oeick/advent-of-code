import unittest

import main

EXAMPLE = [
    [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
    [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
    [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
    [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
    [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]]


class ExampleTests(unittest.TestCase):

    solver: main.Solver

    @classmethod
    def setUpClass(cls):
        cls.solver = main.Solver(EXAMPLE)

    def test_example(self):
        self.assertEqual(
            15,
            self.solver.sum_risk_levels())

    def test_get_all_basins(self):
        self.assertEqual(4, len(self.solver.get_all_basins()))

    def test_get_sizes_of_the_three_largest_basins(self):
        basins = self.solver.get_all_basins()
        self.assertEqual(
            [9, 9, 14],
            main.get_sizes_of_the_three_largest_basins(basins))

    def test_multiply_sizes_of_three_largest_basins(self):
        self.assertEqual(
            1134,
            self.solver.multiply_sizes_of_three_largest_basins())
