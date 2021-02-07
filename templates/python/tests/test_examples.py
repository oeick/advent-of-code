import unittest
import main


class ExampleTests(unittest.TestCase):

    def test_example(self):
        result = main.solve(["test", "123"])
        self.assertEqual((2, 4), result)
