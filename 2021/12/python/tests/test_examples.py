import unittest

import main


class ExampleTests(unittest.TestCase):

    def test_example_1(self):
        example_map = main.map_caves([('start', 'A'),
                                      ('start', 'b'),
                                      ('A', 'c'),
                                      ('A', 'b'),
                                      ('b', 'd'),
                                      ('A', 'end'),
                                      ('b', 'end')])
        self.assertEqual(10, main.Solver(example_map).solve_part_1())
        self.assertEqual(36, main.Solver(example_map).solve_part_2())

    def test_example_2(self):
        example_map = main.map_caves([('dc', 'end'),
                                      ('HN', 'start'),
                                      ('start', 'kj'),
                                      ('dc', 'start'),
                                      ('dc', 'HN'),
                                      ('LN', 'dc'),
                                      ('HN', 'end'),
                                      ('kj', 'sa'),
                                      ('kj', 'HN'),
                                      ('kj', 'dc')])
        self.assertEqual(19, main.Solver(example_map).solve_part_1())
        self.assertEqual(103, main.Solver(example_map).solve_part_2())

    def test_example_3(self):
        example_map = main.map_caves([('fs', 'end'),
                                      ('he', 'DX'),
                                      ('fs', 'he'),
                                      ('start', 'DX'),
                                      ('pj', 'DX'),
                                      ('end', 'zg'),
                                      ('zg', 'sl'),
                                      ('zg', 'pj'),
                                      ('pj', 'he'),
                                      ('RW', 'he'),
                                      ('fs', 'DX'),
                                      ('pj', 'RW'),
                                      ('zg', 'RW'),
                                      ('start', 'pj'),
                                      ('he', 'WI'),
                                      ('zg', 'he'),
                                      ('pj', 'fs'),
                                      ('start', 'RW')])
        self.assertEqual(226, main.Solver(example_map).solve_part_1())
        self.assertEqual(3509, main.Solver(example_map).solve_part_2())
