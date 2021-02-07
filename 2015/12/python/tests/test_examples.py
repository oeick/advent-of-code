import unittest
from parameterized import parameterized
import main


class ExampleTests(unittest.TestCase):

    @parameterized.expand([
        ['[1,2,3]', 6],
        ['{"a":2,"b":4}', 6],
        ['[[[3]]]', 3],
        ['{"a":{"b":4},"c":-1}', 3],
        ['{"a":[-1,1]}', 0],
        ['[-1,{"a":1}]', 0],
        ['[]', 0],
        ['{}', 0]
    ])
    def test_example(self, input_str, expected_sum):
        self.assertEqual(expected_sum, main.solve(input_str))
