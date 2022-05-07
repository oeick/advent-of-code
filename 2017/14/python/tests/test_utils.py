import unittest
import main
from main import Coords


class UtilTests(unittest.TestCase):

    def test_hex2bin(self):
        self.assertEqual(
            '1010000011000010000000010111',
            main.hex2bin('a0c2017'))

    def test_equal_coords(self):
        self.assertEqual(
            Coords(1, 0),
            Coords(1, 0))

    def test_find_group_small(self):
        grid = ['110',
                '010']
        self.assertEqual(
            {Coords(0, 0), Coords(0, 1), Coords(1, 1)},
            main.find_group(Coords(0, 0), grid))

    def test_find_group_large(self):
        grid = ['11010101',
                '01000101',
                '01111101',
                '00000010',
                '11111111']
        self.assertEqual(
            {Coords(0, 0), Coords(0, 1), Coords(1, 1), Coords(2, 1),
             Coords(2, 2), Coords(2, 3), Coords(2, 4), Coords(2, 5),
             Coords(1, 5), Coords(0, 5)},
            main.find_group(Coords(2, 3), grid))

    def test_find_groups_small(self):
        grid = ['101']
        self.assertEqual(
            [{Coords(0, 0), }, {Coords(0, 2), }],
            main.find_groups(grid))

    def test_find_groups_large(self):
        grid = ['10101',
                '10001',
                '11111']
        self.assertEqual(
            [
                {Coords(0, 0), Coords(1, 0), Coords(2, 0),
                 Coords(2, 1), Coords(2, 2), Coords(2, 3),
                 Coords(2, 4), Coords(1, 4), Coords(0, 4)},
                {Coords(0, 2), }
            ],
            main.find_groups(grid))
