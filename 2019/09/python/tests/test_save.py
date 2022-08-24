import unittest

from computer import Computer


class SaveTests(unittest.TestCase):

    def test_position_mode(self):
        cmp = Computer({0: 3, 1: 2, 2: 0}, [99, ])
        cmp.run()
        self.assertEqual(99, cmp.program[2])

    def test_immediate_mode(self):
        cmp = Computer({0: 103, 1: 2, 2: 0}, [99, ])
        self.assertRaises(ValueError, cmp.run)

    def test_relative_mode(self):
        cmp = Computer({0: 109, 1: 9, 2: 203, 3: -5, 4: 0}, [99, ])
        cmp.run()
        self.assertEqual(99, cmp.program[4])
