import unittest
import main


class ExampleTests(unittest.TestCase):

    def test_example(self):
        result = main.solve([
            '1-3 a: abcde',
            '1-3 b: cdefg',
            '2-9 c: ccccccccc'])
        self.assertEqual(result[0], 2)
        self.assertEqual(result[1], 1)
