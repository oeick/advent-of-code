import unittest
import main

TESTNODES = main.create_nodes(
    [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2])


class ExampleTests(unittest.TestCase):

    def test_example_part_1(self):
        self.assertEqual(138, main.solve_part_1(TESTNODES))

    def test_example_part_2(self):
        self.assertEqual(66, main.solve_part_2(TESTNODES))
