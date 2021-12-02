import unittest
import main


class ExampleTests(unittest.TestCase):

    def test_example_1(self):
        result = main.solve_part_1(
            [('forward', 5),
             ('down', 5),
             ('forward', 8),
             ('up', 3),
             ('down', 8),
             ('forward', 2)])
        self.assertEqual(150, result)

    def test_example_2(self):
        result = main.solve_part_2(
            [('forward', 5),
             ('down', 5),
             ('forward', 8),
             ('up', 3),
             ('down', 8),
             ('forward', 2)])
        self.assertEqual(900, result)
