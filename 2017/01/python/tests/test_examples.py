import unittest
import main
from parameterized import parameterized


class ExampleTests(unittest.TestCase):

    @parameterized.expand((
        (3, '1122'),
        (4, '1111'),
        (0, '1234'),
        (9, '91212129'),
    ))
    def test_part_1(self, expected, captcha):
        self.assertEqual(expected, main.solve_part_1(captcha))

    @parameterized.expand((
        (6, '1212'),
        (0, '1221'),
        (4, '123425'),
        (12, '123123'),
        (4, '12131415'),
    ))
    def test_part_2(self, expected, captcha):
        self.assertEqual(expected, main.solve_part_2(captcha))