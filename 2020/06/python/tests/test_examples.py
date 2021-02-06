import unittest
import main


class ExampleTests(unittest.TestCase):

    def test_empty_input(self):
        solution_1, solution_2 = main.solve([])
        self.assertEqual(0, solution_1)
        self.assertEqual(0, solution_2)

    def test_empty_line(self):
        solution_1, solution_2 = main.solve([''])
        self.assertEqual(0, solution_1)
        self.assertEqual(0, solution_2)

    def test_no_empty_last_line(self):
        lines = ['abc',
                 '',
                 'ab',
                 'ac']
        solution_1, solution_2 = main.solve(lines)
        self.assertEqual(6, solution_1)
        self.assertEqual(4, solution_2)

    def test_one_empty_last_line(self):
        lines = ['abc',
                 '',
                 'ab',
                 'ac',
                 '']
        solution_1, solution_2 = main.solve(lines)
        self.assertEqual(6, solution_1)
        self.assertEqual(4, solution_2)

    def test_two_empty_last_lines(self):
        lines = ['abc',
                 '',
                 'ab',
                 'ac',
                 '',
                 '']
        solution_1, solution_2 = main.solve(lines)
        self.assertEqual(6, solution_1)
        self.assertEqual(4, solution_2)

    def test_example(self):
        example = """
        abc
                     
        a
        b
        c
        
        ab
        ac
        
        a
        a
        a
        a
        
        b
        """
        lines = [line.strip() for line in example.splitlines()]
        solution_1, solution_2 = main.solve(lines)
        self.assertEqual(11, solution_1)
        self.assertEqual(6, solution_2)
