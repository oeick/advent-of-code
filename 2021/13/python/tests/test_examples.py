import unittest

import main

EXAMPLE = ['6,10',
           '0,14',
           '9,10',
           '0,3',
           '10,4',
           '4,11',
           '6,0',
           '6,12',
           '4,1',
           '0,13',
           '10,12',
           '3,4',
           '3,0',
           '8,4',
           '1,10',
           '2,14',
           '8,10',
           '9,0',
           '',
           'fold along y=7',
           'fold along x=5']


class ExampleTests(unittest.TestCase):

    def test_example(self):
        dots = [p for p in main.parse_dot(EXAMPLE)]
        instructions = [i for i in main.parse_instruction(EXAMPLE)]
        self.assertEqual(17, main.solve_part_1(dots, instructions[0]))
        self.assertEqual(
            '#####\n'
            '#...#\n'
            '#...#\n'
            '#...#\n'
            '#####',
            main.solve_part_2(dots, instructions))

