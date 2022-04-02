import unittest
import main
from parameterized import parameterized


class ExampleTests(unittest.TestCase):

    @parameterized.expand((
            (True, 'aa bb cc dd ee'),
            (False, 'aa bb cc dd aa'),
            (True, 'aa bb cc dd aaa'),
    ))
    def test_has_no_duplicates(self, expected, phrase):
        self.assertEqual(expected, main.has_no_duplicates(phrase))

    @parameterized.expand((
            (True, 'abcde fghij'),
            (False, 'abcde xyz ecdab'),
            (True, 'a ab abc abd abf abj'),
            (True, 'iiii oiii ooii oooi oooo'),
            (False, 'oiii ioii iioi iiio')
    ))
    def test_has_no_anagrams(self, expected, phrase):
        self.assertEqual(expected, main.has_no_anagrams(phrase))
