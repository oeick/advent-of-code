import unittest
import main
from parameterized import parameterized


class ExampleTests(unittest.TestCase):

    def test_part_1_example(self):
        self.assertEqual(3, main.solve_part_1([1, -2, 3, 1]))

    @parameterized.expand([
        (2, [1, -2, 3, 1]),
        (0, [1, -1]),
        (10, [3, 3, 4, -2, -4]),
        (5, [-6, 3, 8, 5, -6]),
        (14, [7, 7, -2, -7, -4]),
    ])
    def test_part_2_examples(self, expected, changes):
        self.assertEqual(expected, main.solve_part_2(changes))
