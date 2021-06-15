import unittest
import main


class ExampleTests(unittest.TestCase):

    def test_calc_index(self):
        self.assertEqual(1, main.calc_index(1, 1))
        self.assertEqual(16, main.calc_index(6, 1))
        self.assertEqual(18, main.calc_index(4, 3))
        self.assertEqual(21, main.calc_index(1, 6))

    def test_calc_code(self):
        self.assertEqual(20151125, main.calc_code(1))
        self.assertEqual(33071741, main.calc_code(16))
        self.assertEqual(21345942, main.calc_code(18))
        self.assertEqual(33511524, main.calc_code(21))

    def test_solve(self):
        self.assertEqual(27995004, main.solve(6, 6))
