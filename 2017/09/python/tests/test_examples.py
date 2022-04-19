import unittest
import main
from parameterized import parameterized


class ExampleTests(unittest.TestCase):

    @parameterized.expand([
        (1, '{}'),
        (6, '{{{}}}'),
        (5, '{{},{}}'),
        (16, '{{{},{},{{}}}}'),
        (1, '{<a>,<a>,<a>,<a>}'),
        (9, '{{<ab>},{<ab>},{<ab>},{<ab>}}'),
        (9, '{{<!!>},{<!!>},{<!!>},{<!!>}}'),
        (3, '{{<a!>},{<a!>},{<a!>},{<ab>}}')
    ])
    def test_part_1(self, score, stream):
        self.assertEqual(score, main.solve_part_1(stream))

    @parameterized.expand([
        (0, '<>'),
        (17, '<random characters>'),
        (3, '<<<<>'),
        (2, '<{!>}>'),
        (0, '<!!>'),
        (0, '<!!!>>'),
        (10, '<{o"i!a,<{i<a>')
    ])
    def test_part_2(self, count, garbage):
        self.assertEqual(count, main.solve_part_2(garbage))
