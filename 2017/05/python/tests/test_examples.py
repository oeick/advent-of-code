import unittest

import main


class ExampleTests(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(5, main.solve_part_1([0, 3, 0, 1, -3]))

    def test_part_2(self):
        self.assertEqual(10, main.solve_part_2([0, 3, 0, 1, -3]))
