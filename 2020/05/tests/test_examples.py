import unittest
import main


class ExampleTests(unittest.TestCase):

    def test_example_row(self):
        result = main.get_row('FBFBBFFRLR')
        self.assertEqual(result, 44)

    def test_example_column(self):
        result = main.get_column('FBFBBFFRLR')
        self.assertEqual(result, 5)

    def test_example_seat_id(self):
        result = main.get_seat_ids(['FBFBBFFRLR'])
        self.assertEqual(result, [357])

    def test_examples_part1(self):
        result = main.get_seat_ids(['BFFFBBFRRR',
                                    'FFFBBBFRRR',
                                    'BBFFBBFRLL'])
        self.assertEqual(result, [567, 119, 820])
