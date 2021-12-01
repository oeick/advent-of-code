import unittest
import main


class ExampleTests(unittest.TestCase):

    def test_example(self):
        solution1, solution2 = main.solve([
            '199',
            '200',
            '208',
            '210',
            '200',
            '207',
            '240',
            '269',
            '260',
            '263',
        ])
        self.assertEqual(7, solution1)
        self.assertEqual(5, solution2)
