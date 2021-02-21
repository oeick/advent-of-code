import unittest
import main


class ExampleTests(unittest.TestCase):

    def test_parser_one_line_positive_value(self):
        lines = ['Alice would gain 54 happiness units by sitting next to Bob.']
        self.assertEqual(
            {'Alice': {'Bob': 54}},
            main.parse_happiness_units(lines))

    def test_parser_one_line_negative_value(self):
        lines = ['Alice would lose 2 happiness units by sitting next to David.']
        self.assertEqual(
            {'Alice': {'David': -2}},
            main.parse_happiness_units(lines))

    def test_parser_two_lines(self):
        lines = ['Alice would gain 54 happiness units by sitting next to Bob.',
                 'Alice would lose 2 happiness units by sitting next to David.']
        self.assertEqual(
            {'Alice': {'Bob': 54, 'David': -2}},
            main.parse_happiness_units(lines))

    def test_append_yourself(self):
        units = {'A': {'B': 1},
                 'B': {'A': 2}}
        self.assertEqual(
            {'A': {'B': 1, 'Yourself': 0},
             'B': {'A': 2, 'Yourself': 0},
             'Yourself': {'A': 0, 'B': 0}},
            main.append_yourself(units)
        )

    def test_calc_happiness(self):
        arrangement = ('A', 'B', 'C', 'D')
        units = {'A': {'B': 1, 'C': 1000, 'D': 2},
                 'B': {'A': 4, 'C': 8, 'D': 1000},
                 'C': {'A': 1000, 'B': 16, 'D': 32},
                 'D': {'A': 64, 'B': 1000, 'C': 128}}
        self.assertEqual(255, main.calc_happiness(arrangement, units))

    def test_example(self):
        example = """
            Alice would gain 54 happiness units by sitting next to Bob.
            Alice would lose 79 happiness units by sitting next to Carol.
            Alice would lose 2 happiness units by sitting next to David.
            Bob would gain 83 happiness units by sitting next to Alice.
            Bob would lose 7 happiness units by sitting next to Carol.
            Bob would lose 63 happiness units by sitting next to David.
            Carol would lose 62 happiness units by sitting next to Alice.
            Carol would gain 60 happiness units by sitting next to Bob.
            Carol would gain 55 happiness units by sitting next to David.
            David would gain 46 happiness units by sitting next to Alice.
            David would lose 7 happiness units by sitting next to Bob.
            David would gain 41 happiness units by sitting next to Carol.
            """
        lines = [line.strip()
                 for line in example.splitlines()
                 if line.strip()]
        result = main.solve_part_1(lines)
        self.assertEqual(330, result)
