import unittest
import main
from parameterized import parameterized


class ExampleTests(unittest.TestCase):

    def test_find_stop_number(self):
        self.assertEqual(1, main.find_stop_number(0))
        self.assertEqual(9, main.find_stop_number(1))
        self.assertEqual(25, main.find_stop_number(2))

    def test_find_rectangle_for(self):
        self.assertEqual(0, main.find_rectangle_for(1))
        self.assertEqual(1, main.find_rectangle_for(2))
        self.assertEqual(1, main.find_rectangle_for(9))
        self.assertEqual(2, main.find_rectangle_for(10))

    def test_get_corner_numbers(self):
        self.assertEqual([1, 1, 1, 1], main.get_corner_numbers(0))
        self.assertEqual([9, 7, 5, 3], main.get_corner_numbers(1))
        self.assertEqual([25, 21, 17, 13], main.get_corner_numbers(2))

    def test_solve_part_1(self):
        self.assertEqual(0, main.solve_part_1(1))
        self.assertEqual(3, main.solve_part_1(12))
        self.assertEqual(2, main.solve_part_1(23))
        self.assertEqual(31, main.solve_part_1(1024))

    @parameterized.expand([
        (2, 1),
        (4, 2),
        (4, 3),
        (5, 4),
        (10, 5),
        (806, 800)])
    def test_solve_part_2(self, expected, square):
        self.assertEqual(expected, main.solve_part_2(square))
