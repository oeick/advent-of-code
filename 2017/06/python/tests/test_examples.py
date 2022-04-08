import unittest
import main


class ExampleTests(unittest.TestCase):

    def test_example_for_both_parts(self):
        self.assertEqual((5, 4), main.solve([0, 2, 7, 0]))
