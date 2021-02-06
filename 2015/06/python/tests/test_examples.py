import unittest
from main import Lights, Rectangle


class ExampleTests(unittest.TestCase):

    def test_part_1_turn_on_all(self):
        lights = Lights(1000)
        lights.turn(Rectangle(0, 0, 999, 999), 1)
        self.assertEqual(1_000_000, lights.count_lit())

    def test_part_1_turn_on_first_line(self):
        lights = Lights(1000)
        lights.turn(Rectangle(0, 0, 999, 0), 1)
        self.assertEqual(1000, lights.count_lit())

    def test_part_1_turn_on_middle_four(self):
        lights = Lights(1000)
        lights.turn(Rectangle(499, 499, 500, 500), 1)
        self.assertEqual(4, lights.count_lit())

    def test_part_2_increase_one_by_1(self):
        lights = Lights(1000)
        lights.increase(Rectangle(0, 0, 0, 0), 1)
        self.assertEqual(1, lights.total_brightness())

    def test_part_2_increase_all_by_2(self):
        lights = Lights(1000)
        lights.increase(Rectangle(0, 0, 999, 999), 2)
        self.assertEqual(2_000_000, lights.total_brightness())
