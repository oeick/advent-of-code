import unittest

import main

EXAMPLE = [
    '00100',
    '11110',
    '10110',
    '10111',
    '10101',
    '01111',
    '00111',
    '11100',
    '10000',
    '11001',
    '00010',
    '01010',
]


class ExampleTests(unittest.TestCase):

    def test_solve_part_1(self):
        self.assertEqual(198, main.solve_part_1(EXAMPLE))

    def test_solve_part_2(self):
        self.assertEqual(230, main.solve_part_2(EXAMPLE))

    def test_get_oxygen_generator_rating(self):
        self.assertEqual('10111', main.get_rating(EXAMPLE, True))

    def test_get_co2_scrubber_rating(self):
        self.assertEqual('01010', main.get_rating(EXAMPLE, False))
