import unittest
from collections import Counter

import main


class ExampleTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        lines = [
            'CH -> B',
            'HH -> N',
            'CB -> H',
            'NH -> C',
            'HB -> C',
            'HC -> B',
            'HN -> C',
            'NN -> C',
            'BH -> H',
            'NC -> B',
            'NB -> B',
            'BN -> B',
            'BB -> N',
            'BC -> B',
            'CC -> N',
            'CN -> C',
        ]
        cls.solver = main.Solver(main.parse_rules(lines))

    def test_count_elements_1(self):
        result = self.solver.count_elements('NNCB', 4)
        self.assertEqual(
            Counter('NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB'),
            result)

    def test_count_elements_2(self):
        result = self.solver.count_elements('NNCB', 10)
        self.assertEqual(
            {'B': 1749, 'N': 865, 'C': 298, 'H': 161},
            result)

    def test_count_elements_3(self):
        result = self.solver.count_elements('NNCB', 40)
        self.assertEqual(2192039569602, result['B'])
        self.assertEqual(3849876073, result['H'])

    def test_solve_part_1(self):
        self.assertEqual(1588, self.solver.solve('NNCB', 10))

    def test_solve_part_2(self):
        self.assertEqual(2188189693529, self.solver.solve('NNCB', 40))
