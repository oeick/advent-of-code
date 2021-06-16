import unittest
import main
from parameterized import parameterized


class ExampleTests(unittest.TestCase):

    def test_solve_part_1(self):
        self.assertEqual(
            295,
            main.solve_part_1(939, "7,13,x,x,59,x,31,19"))

    @parameterized.expand([
        [1068781, "7,13,x,x,59,x,31,19"],
        [3417, "17,x,13,19"],
        [754018, "67,7,59,61"],
        [779210, "67,x,7,59,61"],
        [1261476, "67,7,x,59,61"],
        [1202161486, "1789,37,47,1889"],
    ])
    def test_solve_part_2(self, expected, ids):
        self.assertEqual(expected, main.solve_part_2(ids))
