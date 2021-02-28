import unittest

import main


class ExampleTests(unittest.TestCase):

    def test_example(self):
        result = main.solve_part_1(
            ['Sue 1: trees: 7, perfumes: 2, akitas: 5',
             'Sue 2: children: 3, goldfish: 4, vizslas: 0',
             'Sue 3: children: 3, goldfish: 5, vizslas: 0']
        )
        self.assertEqual(3, result)
