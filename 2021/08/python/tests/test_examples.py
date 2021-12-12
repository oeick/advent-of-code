import unittest

import main
from main import Wiring

EXAMPLE = [
    'be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb |'
    'fdgacbe cefdb cefbgd gcbe',
    'edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec |'
    'fcgedb cgb dgebacf gc',
    'fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef |'
    'cg cg fdcagb cbg',
    'fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega |'
    'efabcd cedba gadfec cb',
    'aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga |'
    'gecf egdcabf bgf bfgea',
    'fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf |'
    'gebdcfa ecba ca fadegcb',
    'dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf |'
    'cefg dcbef fcge gbcadfe',
    'bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd |'
    'ed bcgafe cdgba cbgef',
    'egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg |'
    'gbdfcae bgc cg cgb',
    'gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc |'
    'fgae cfgab fg bagce']


class ExampleTests(unittest.TestCase):

    example: list[Wiring]

    @classmethod
    def setUpClass(cls):
        cls.example = [main.parse(line) for line in EXAMPLE]

    def test_example(self):
        self.assertEqual(26, main.solve_part_1(self.example))

    def test_solve2(self):
        self.assertEqual(61229, main.solve_part_2(self.example))
