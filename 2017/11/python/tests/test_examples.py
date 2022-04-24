import unittest
import main
from parameterized import parameterized


class ExampleTests(unittest.TestCase):

    @parameterized.expand([
        (3, ['ne', 'ne', 'ne']),
        (0, ['ne', 'ne', 'sw', 'sw']),
        (2, ['ne', 'ne', 's', 's']),
        (3, ['se', 'sw', 'se', 'sw', 'sw'])
    ])
    def test_example(self, expected, steps):
        self.assertEqual(expected, main.solve(steps)[0])

    @parameterized.expand([
        (0, (0, 0)),
        (1, (0, 1)),
        (1, (1, 0)),
        (1, (1, -1)),
        (1, (0, -1)),
        (1, (-1, 0)),
        (1, (-1, 1)),
        (3, (0, 3)),
        (3, (1, 2)),
        (3, (2, 1)),
        (3, (3, 0)),
        (3, (3, -1)),
        (3, (3, -2)),
        (3, (3, -3)),
        (3, (2, -3)),
        (3, (1, -3)),
        (3, (0, -3)),
        (3, (-1, -2)),
        (3, (-2, -1)),
        (3, (-3, 0)),
        (3, (-3, 1)),
        (3, (-3, 2)),
        (3, (-3, 3)),
        (3, (-2, 3)),
        (3, (-1, 3))])
    def test_calc_distance(self, expected, coords):
        self.assertEqual(expected, main.calc_distance(coords))
