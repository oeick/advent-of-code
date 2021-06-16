import unittest
import main
from parameterized import parameterized


class ExampleTests(unittest.TestCase):

    @parameterized.expand([
        (5, ["R2", "L3"]),
        (2, ["R2", "R2", "R2"]),
        (12, ["R5", "L5", "R5", "R3"]),
    ])
    def test_part_1_examples(self, expected, instructions):
        self.assertEqual(expected, main.solve(instructions)[0])

    def test_part_2_example(self):
        self.assertEqual(4, main.solve(["R8", "R4", "R4", "R8"])[1])
