import unittest
import main


class ExampleTests(unittest.TestCase):

    def test_example(self):
        target = main.parse('target area: x=20..30, y=-10..-5')
        self.assertEqual((45, 112), main.solve(target))
