import unittest
import main
from parameterized import parameterized

GRID = main.build_grid('flqrgnkx')


class GridTests(unittest.TestCase):

    @parameterized.expand([(0, '11010100'),
                           (1, '01010101'),
                           (2, '00001010'),
                           (3, '10101101'),
                           (4, '01101000'),
                           (5, '11001001'),
                           (6, '01000100'),
                           (7, '11010110')])
    def test_build_grid(self, row, expected):
        self.assertTrue(expected, GRID[row])

    def test_solve_part_1(self):
        self.assertEqual(
            8108,
            main.solve_part_1(GRID))

    def test_solve_part_2(self):
        self.assertEqual(
            1242,
            main.solve_part_2(GRID))
