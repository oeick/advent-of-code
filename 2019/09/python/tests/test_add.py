import unittest

from computer import Computer


class AddTests(unittest.TestCase):

    def test_position_mode(self):
        cmp = Computer({0: 1, 1: 0, 2: 4, 3: 4, 4: 98}, [])
        cmp.run()
        self.assertEqual(99, cmp.program[4])

    def test_immediate_mode(self):
        cmp = Computer({0: 1101, 1: 44, 2: 55, 3: 4, 4: 0}, [])
        cmp.run()
        self.assertEqual(99, cmp.program[4])

    def test_relative_mode(self):
        cmp = Computer(
            {0: 209, 1: 8, 2: 22201, 3: -7, 4: 0, 5: -1, 6: 0, 7: -110, 8: 7},
            [])
        cmp.run()
        self.assertEqual(99, cmp.program[6])
