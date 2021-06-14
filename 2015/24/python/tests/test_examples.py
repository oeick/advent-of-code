import unittest
import main


class ExampleTests(unittest.TestCase):

    def test_example_part_1(self):
        self.assertEqual(
            99,
            main.solve(
                [1, 2, 3, 4, 5, 7, 8, 9, 10, 11],
                3
            )
        )

    def test_example_part_2(self):
        self.assertEqual(
            44,
            main.solve(
                [1, 2, 3, 4, 5, 7, 8, 9, 10, 11],
                4
            )
        )

