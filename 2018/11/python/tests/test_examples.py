import unittest

from parameterized import parameterized

import main


class ExampleTests(unittest.TestCase):

    @parameterized.expand([
        (3, 5, 8, 4),
        (122, 79, 57, -5),
        (217, 196, 39, 0),
        (101, 153, 71, 4)])
    def test_examples_part_1_calculate_power_level(
            self, x, y, serial_number, expected):
        self.assertEqual(
            expected, main.calculate_power_level(x, y, serial_number))

    @parameterized.expand([
        (18, 33, 45, 29),
        (42, 21, 61, 30)])
    def test_examples_part_1_find_max_power_square(
            self, grid_serial_number, x, y, power):
        self.assertEqual(
            (x, y, power),
            main.find_max_power_square(
                main.calculate_power_level_array(grid_serial_number)))

    @parameterized.expand([
        (18, 16, 90, 269, 113),
        (42, 12, 232, 251, 119)])
    def test_examples_part_2_find_max_power_square(
            self, grid_serial_number, square_size, x, y, power):
        self.assertEqual(
            (x, y, power),
            main.find_max_power_square(
                main.calculate_power_level_array(grid_serial_number),
                square_size=square_size))
