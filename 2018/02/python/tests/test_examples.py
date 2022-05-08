import unittest
import main
from parameterized import parameterized


class ExampleTests(unittest.TestCase):

    @parameterized.expand([
        ((0, 0), 'abcdef'),
        ((1, 1), 'bababc'),
        ((1, 0), 'abbcde'),
        ((0, 1), 'abcccd'),
        ((1, 0), 'aabcdd'),
        ((1, 0), 'abcdee'),
        ((0, 1), 'ababab')])
    def test_count_double_and_triple_chars(self, expected, string):
        self.assertEqual(
            expected,
            main.count_double_and_triple_chars([string]))

    def test_example_part_1(self):
        self.assertEqual(
            12,
            main.solve_part_1(['abcdef',
                               'bababc',
                               'abbcde',
                               'abcccd',
                               'aabcdd',
                               'abcdee',
                               'ababab']))

    def test_example_part_2(self):
        self.assertEqual(
            'fgij',
            main.solve_part_2(['abcde',
                               'fghij',
                               'klmno',
                               'pqrst',
                               'fguij',
                               'axcye',
                               'wvxyz']))
