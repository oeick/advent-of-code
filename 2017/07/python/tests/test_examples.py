import unittest

import main

TEST_DATA = ["pbga (66)",
             "xhth (57)",
             "ebii (61)",
             "havc (66)",
             "ktlj (57)",
             "fwft (72) -> ktlj, cntj, xhth",
             "qoyq (66)",
             "padx (45) -> pbga, havc, qoyq",
             "tknk (41) -> ugml, padx, fwft",
             "jptl (61)",
             "ugml (68) -> gyxo, ebii, jptl",
             "gyxo (61)",
             "cntj (57)"]


class ExampleTests(unittest.TestCase):

    def test_part_1(self):
        programs = main.create_tree(TEST_DATA)
        self.assertEqual("tknk", main.solve_part_1(programs))

    def test_part_2(self):
        programs = main.create_tree(TEST_DATA)
        self.assertEqual(60, main.solve_part_2(programs))

    def test_calc_total_weight(self):
        programs = main.create_tree(TEST_DATA)
        self.assertEqual(251, main.calc_total_weight('ugml', programs))
        self.assertEqual(243, main.calc_total_weight('padx', programs))
        self.assertEqual(243, main.calc_total_weight('fwft', programs))
