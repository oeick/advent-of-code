import unittest
import main


class ExampleTests(unittest.TestCase):

    def test_example_part_1(self):
        self.assertEqual(
            ['123456', '789012'],
            main.get_layers('123456789012', (3, 2)))

    def test_example_part_2(self):
        layers_lines = main.get_lines_of_layers(
            ['0222', '1122', '2212', '0000'], (2, 2))
        self.assertEqual(
            ['01', '10'],
            main.stack_lines(layers_lines, (2, 2)))
