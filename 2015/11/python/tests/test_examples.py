import unittest
from parameterized import parameterized
import main


class ExampleTests(unittest.TestCase):

    @parameterized.expand([
        ['hijklmmn'],
        ['abbceffg'],
        ['abbcegjk']
    ])
    def test_invalid_passwords(self, password):
        self.assertFalse(main.is_valid(password))

    def test_quick_example(self):
        result = main.solve('abcdefgh')
        self.assertEqual('abcdffaa', result)

    def test_tedious_example(self):
        result = main.solve('ghijklmn')
        self.assertEqual('ghjaabcc', result)
