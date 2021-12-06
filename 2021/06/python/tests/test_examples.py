import unittest

import main


class ExampleTests(unittest.TestCase):

    def test_example_18(self):
        self.assertEqual(26, main.solve([3, 4, 3, 1, 2], 18))

    def test_example_80(self):
        self.assertEqual(5934, main.solve([3, 4, 3, 1, 2], 80))
