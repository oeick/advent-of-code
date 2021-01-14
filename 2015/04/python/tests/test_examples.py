import unittest
import main


class ExampleTests(unittest.TestCase):

    def test_example_1(self):
        secret_key = 'abcdef'
        result = main.solve_part1(secret_key)
        self.assertEqual(result, 609043)

    def test_example_2(self):
        secret_key = 'pqrstuv'
        result = main.solve_part1(secret_key)
        self.assertEqual(result, 1048970)
