import unittest
import main


class ExampleTests(unittest.TestCase):

    def test_example_part1(self):
        numbers = [1721, 979, 366, 299, 675, 1456]
        result = main.solve(numbers, 2)
        self.assertEqual(result, 514579)

    def test_example_part2(self):
        numbers = [1721, 979, 366, 299, 675, 1456]
        result = main.solve(numbers, 3)
        self.assertEqual(result, 241861950)
