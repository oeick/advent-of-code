import unittest

import main

EXAMPLE = """
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi""".splitlines()[1:]


class ExampleTests(unittest.TestCase):

    def test_example_part_1(self):
        area = main.parse_area(EXAMPLE)
        self.assertEqual(31, main.solve_part_1(area))

    def test_example_part_2(self):
        area = main.parse_area(EXAMPLE)
        self.assertEqual(29, main.solve_part_2(area))
