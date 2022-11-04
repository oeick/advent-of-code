import unittest

import main
from light import Light


class ExampleTests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(
            ("""
#...#..###
#...#...#.
#...#...#.
#####...#.
#...#...#.
#...#...#.
#...#...#.
#...#..###"""[1:], 3),
            main.solve([Light((9, 1), (0, 2)),
                        Light((7, 0), (-1, 0)),
                        Light((3, -2), (-1, 1)),
                        Light((6, 10), (-2, -1)),
                        Light((2, -4), (2, 2)),
                        Light((-6, 10), (2, -2)),
                        Light((1, 8), (1, -1)),
                        Light((1, 7), (1, 0)),
                        Light((-3, 11), (1, -2)),
                        Light((7, 6), (-1, -1)),
                        Light((-2, 3), (1, 0)),
                        Light((-4, 3), (2, 0)),
                        Light((10, -3), (-1, 1)),
                        Light((5, 11), (1, -2)),
                        Light((4, 7), (0, -1)),
                        Light((8, -2), (0, 1)),
                        Light((15, 0), (-2, 0)),
                        Light((1, 6), (1, 0)),
                        Light((8, 9), (0, -1)),
                        Light((3, 3), (-1, 1)),
                        Light((0, 5), (0, -1)),
                        Light((-2, 2), (2, 0)),
                        Light((5, -2), (1, 2)),
                        Light((1, 4), (2, 1)),
                        Light((-2, 7), (2, -2)),
                        Light((3, 6), (-1, -1)),
                        Light((5, 0), (1, 0)),
                        Light((-6, 0), (2, 0)),
                        Light((5, 9), (1, -2)),
                        Light((14, 7), (-2, 0)),
                        Light((-3, 6), (2, -1))]))
