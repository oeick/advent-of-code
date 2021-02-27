import unittest
import main
from parameterized import parameterized


class ExampleTests(unittest.TestCase):

    @parameterized.expand([
        ('(())', 0),
        ('()()', 0),
        ('(((', 3),
        ('(()(()(', 3),
        ('))(((((', 3),
        ('())', -1),
        ('))(', -1),
        (')))', -3),
        (')())())', -3)
    ])
    def test_example_part1(self, example, floor):
        self.assertEqual(floor, main.solve_part_1(example))

    def test_example_part2(self):
        self.assertEqual(1, main.solve_part_2(')'))
        self.assertEqual(5, main.solve_part_2('()())'))
