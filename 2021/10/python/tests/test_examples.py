import unittest

import main


class ExampleTests(unittest.TestCase):

    def test_solve_part_1(self):
        self.assertEqual(
            26397,
            main.solve_part_1([
                '{([(<{}[<>[]}>{[]{[(<()>',
                '[[<[([]))<([[{}[[()]]]',
                '[{[{({}]{}}([{[{{{}}([]',
                '[<(<(<(<{}))><([]([]()',
                '<{([([[(<>()){}]>(<<{{']))

    def test_solve_part_2(self):
        self.assertEqual(
            288957,
            main.solve_part_2([
                '[({(<(())[]>[[{[]{<()<>>',
                '[(()[<>])]({[<{<<[]>>(',
                '(((({<>}<{<{<>}{[]{[]{}',
                '{<[[]]>}<{[{[{[]{()[[[]',
                '<{([{{}}[<[[[<>{}]]]>[]]']))
