import unittest
import main
from parameterized import parameterized


class ExampleTests(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(12, main.solve_part_1(range(5), [3, 4, 1, 5]))

    @parameterized.expand([
        ('', 'a2582a3a0e66e6e86e3812dcb672a272'),
        ('AoC 2017', '33efeb34ea91902bb2f59c9920caa6cd'),
        ('1,2,3', '3efbe78a8d82f29979031a4aa0b16a9d'),
        ('1,2,4', '63960835bcdc130f0b66d7ff4f6a5a8e')
    ])
    def test_part_2(self, input_string, expected):
        self.assertEqual(expected, main.solve_part_2(range(256), input_string))
