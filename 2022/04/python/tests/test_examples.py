import unittest
import main


class ExampleTests(unittest.TestCase):

    def test_example(self):
        result = main.solve(main.parse_pairs([
            "2-4,6-8",
            "2-3,4-5",
            "5-7,7-9",
            "2-8,3-7",
            "6-6,4-6",
            "2-6,4-8"]))
        self.assertEqual((2, 4), result)
