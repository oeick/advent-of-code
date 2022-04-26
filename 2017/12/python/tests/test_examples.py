import unittest
import main

EXAMPLE = [{2}, {1}, {0, 3, 4}, {2, 4}, {2, 3, 6}, {6}, {4, 5}]


class ExampleTests(unittest.TestCase):

    def test_parse_line(self):
        self.assertEqual(
            {0, 3, 4},
            main.parse_line('2 <-> 0, 3, 4'))

    def test_find_group_members_0(self):
        self.assertEqual({0, 2, 3, 4, 5, 6}, main.find_group_members(EXAMPLE))

    def test_find_group_members_1(self):
        self.assertEqual({1}, main.find_group_members(EXAMPLE, start_member=1))

    def test_find_groups(self):
        self.assertEqual([{0, 2, 3, 4, 5, 6}, {1}], main.find_groups(EXAMPLE))

    def test_solve_part_1(self):
        self.assertEqual(6, main.solve_part_1(EXAMPLE))

    def test_solve_part_2(self):
        self.assertEqual(2, main.solve_part_2(EXAMPLE))
