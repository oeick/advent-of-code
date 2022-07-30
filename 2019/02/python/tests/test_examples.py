import unittest

from parameterized import parameterized

import main


class ExampleTests(unittest.TestCase):

    @parameterized.expand([
        ([3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50],
         [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]),

        ([2, 0, 0, 0, 99],
         [1, 0, 0, 0, 99]),

        ([2, 3, 0, 6, 99],
         [2, 3, 0, 3, 99]),

        ([2, 4, 4, 5, 99, 9801],
         [2, 4, 4, 5, 99, 0]),

        ([30, 1, 1, 4, 2, 5, 6, 0, 99],
         [1, 1, 1, 4, 99, 5, 6, 0, 99])
    ])
    def test_examples(self, expected, program):
        self.assertEqual(expected, main.execute_opcodes(program))
