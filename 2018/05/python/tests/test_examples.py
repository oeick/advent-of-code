import unittest
import main

from parameterized import parameterized


class ExampleTests(unittest.TestCase):

    @parameterized.expand([
        ('', 'Aa'),
        ('', 'abBA'),
        ('abAB', 'abAB'),
        ('aabAAB', 'aabAAB'),
        ('dabCBAcaDA', 'dabAcCaCBAcCcaDA')
    ])
    def test_part_1_examples(self, expected, polymer):
        self.assertEqual(expected, main.remove_opposites(polymer))

    def test_part_2_example(self):
        self.assertEqual(
            'daDA',
            main.find_shortest_polymer_with_removed_unit_type(
                'dabAcCaCBAcCcaDA'))
