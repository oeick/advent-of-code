import unittest

import main
from main import Replacement


class ExampleTests(unittest.TestCase):

    def test_parse_lines(self):
        self.assertEqual((
            [('H', 'HO'),
             ('H', 'OH'),
             ('O', 'HH')],
            'HOH'),
            main.parse_lines([
                "H => HO\n",
                "H => OH\n",
                "O => HH\n",
                "\n",
                "HOH"
            ]))

    def test_find_replacement_positions(self):
        self.assertEqual(
            [0, 2],
            main.find_replacement_positions(
                Replacement('H', 'HO'),
                'HOHO'))

    def test_find_replacement_positions_overlapping(self):
        self.assertEqual(
            [0, 1],
            main.find_replacement_positions(
                Replacement('HH', 'O'),
                'HHH'))

    def test_all_replacement_possibilities(self):
        self.assertEqual(
            ['HOOH', 'HOHO'],
            main.find_replacement_possibilities(Replacement('H', 'HO'), 'HOH'))
        self.assertEqual(
            ['OHOH', 'HOOH'],
            main.find_replacement_possibilities(Replacement('H', 'OH'), 'HOH'))
        self.assertEqual(
            ['HHHH'],
            main.find_replacement_possibilities(Replacement('O', 'HH'), 'HOH'))

    def test_find_distinct_molecules_from_examples(self):
        self.assertEqual(
            {'HOOH', 'HOHO', 'OHOH', 'HHHH'},
            main.find_distinct_molecules(
                [Replacement('H', 'OH'),
                 Replacement('H', 'HO'),
                 Replacement('O', 'HH')],
                'HOH'))

    def test_find_distinct_molecules_enhanced(self):
        self.assertEqual(
            {'cxyzc', 'ddabc', 'cabdd'},
            main.find_distinct_molecules(
                [Replacement('ab', 'xyz'),
                 Replacement('c', 'dd')],
                'cabc'))

    def test_solve_part_1(self):
        self.assertEqual(
            4,
            main.solve_part_1(
                [Replacement('H', 'HO'),
                 Replacement('H', 'OH'),
                 Replacement('O', 'HH')],
                'HOH'))

    def test_solve_part_2_example_1(self):
        self.assertEqual(
            4,
            main.solve_part_2(
                [Replacement('e', 'H'),
                 Replacement('e', 'O'),
                 Replacement('H', 'HO'),
                 Replacement('H', 'OH'),
                 Replacement('O', 'HH')],
                'HOHO'))

    def test_solve_part_2_example_2(self):
        self.assertEqual(
            6,
            main.solve_part_2(
                [Replacement('e', 'H'),
                 Replacement('e', 'O'),
                 Replacement('H', 'HO'),
                 Replacement('H', 'OH'),
                 Replacement('O', 'HH')],
                'HOHOHO'))
