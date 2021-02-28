import unittest
import main


class ExampleTests(unittest.TestCase):

    def test_get_combinations(self):
        self.assertEqual(
            [[3, 7]],
            main.get_combinations(10, [1, 3, 5, 7]))
        self.assertEqual(
            [[2, 10], [4, 8]],
            main.get_combinations(12, [2, 4, 8, 10]))

    def test_example_part_1(self):
        self.assertEqual(
            [[5, 5, 15],
             [5, 20],
             [5, 20],
             [10, 15]],
            main.get_all_combinations(
                25,
                [20, 15, 10, 5, 5]))

    def test_example_part_2(self):
        self.assertEqual(
            [[5, 20],
             [5, 20],
             [10, 15]],
            main.get_shortest_combinations(
                main.get_all_combinations(
                    25,
                    [20, 15, 10, 5, 5]))
        )