import unittest

import main


class ExampleTests(unittest.TestCase):

    def test_parse_lines(self):
        result = main.parse_lines([
            "H => HO\n",
            "H => OH\n",
            "O => HH\n",
            "\n",
            "HOH"
        ])
        self.assertEqual((
            [('H', 'HO'),
             ('H', 'OH'),
             ('O', 'HH')],
            'HOH'),
            result)

    def test_all_replacement_possibilities(self):
        self.assertEqual(
            main.find_replacement_possibilities(('H', 'HO'), 'HOH'),
            ['HOOH', 'HOHO'])
        self.assertEqual(
            main.find_replacement_possibilities(('H', 'OH'), 'HOH'),
            ['OHOH', 'HOOH'])
        self.assertEqual(
            main.find_replacement_possibilities(('O', 'HH'), 'HOH'),
            ['HHHH'])

    def test_find_distinct_molecules(self):
        result = main.find_distinct_molecules([
            ('H', 'HO'),
            ('H', 'OH'),
            ('O', 'HH')],
            'HOH')
        self.assertEqual(result, {'HOOH', 'HOHO', 'OHOH', 'HHHH'})

    def test_solve_part_1(self):
        result = main.solve_part_1([
            ('H', 'HO'),
            ('H', 'OH'),
            ('O', 'HH')],
            'HOH')
        self.assertEqual(result, 4)
