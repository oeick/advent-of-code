import unittest
from parameterized import parameterized
import main


class ExampleTests(unittest.TestCase):

    @parameterized.expand([
        ['1', '11'],
        ['11', '21'],
        ['21', '1211'],
        ['1211', '111221'],
        ['111221', '312211']
    ])
    def test_example(self, input_sequence, expected_sequence):
        self.assertEqual(
            expected_sequence,
            main.look_and_say(input_sequence))
