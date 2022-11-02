import unittest

from parameterized import parameterized

import main


class ExampleTests(unittest.TestCase):

    @parameterized.expand([
        (9, 25, 32),
        (10, 1618, 8317),
        (13, 7999, 146373),
        (17, 1104, 2764),
        (21, 6111, 54718),
        (30, 5807, 37305)])
    def test_example(self, n_players, last_marble, expected):
        self.assertEqual(expected, main.solve(n_players, last_marble)[0])
