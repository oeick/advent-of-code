import unittest

from parameterized import parameterized

import main


class ExampleTests(unittest.TestCase):

    @parameterized.expand([
        (1, [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]),
        (0, [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]),
        (1, [3, 3, 1108, -1, 8, 3, 4, 3, 99]),
        (0, [3, 3, 1107, -1, 8, 3, 4, 3, 99])])
    def test_compare_to_value_8(self, expected, program):
        computer = main.Computer(program, 8)
        computer.run()
        self.assertEqual(expected, computer.out)

    @parameterized.expand([
        (999, 7),
        (1000, 8),
        (1001, 9)])
    def test_larger_example(self, expected, inp):
        computer = main.Computer(
            [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
             1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
             999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99],
            inp)
        computer.run()
        self.assertEqual(expected, computer.out)


class FunctionTests(unittest.TestCase):

    def test_multiply_function(self):
        computer = main.Computer([1002, 4, 3, 4, 33], 0)
        computer.run()
        self.assertEqual([1002, 4, 3, 4, 99], computer.program)

    def test_save_function(self):
        computer = main.Computer([3, 2, 0], 99)
        computer.run()
        self.assertEqual([3, 2, 99], computer.program)

    def test_output_function_in_immediate_mode(self):
        computer = main.Computer([104, -42, 99], 0)
        computer.run()
        self.assertEqual(-42, computer.out)

    def test_output_function_in_position_mode(self):
        computer = main.Computer([4, 0, 99], 0)
        computer.run()
        self.assertEqual(4, computer.out)

    def test_jump_if_true_function_negative(self):
        computer = main.Computer([1105, 0, 55, 104, 77, 99], 0)
        computer.run()
        self.assertEqual(77, computer.out)

    def test_jump_if_true_function_positive(self):
        computer = main.Computer([1105, 1, 5, 104, 77, 99], 0)
        computer.run()
        self.assertEqual(0, computer.out)

    def test_jump_if_false_function_negative(self):
        computer = main.Computer([1106, 1, 55, 104, 77, 99], 0)
        computer.run()
        self.assertEqual(77, computer.out)

    def test_jump_if_false_function_positive(self):
        computer = main.Computer([1106, 0, 5, 104, 77, 99], 0)
        computer.run()
        self.assertEqual(0, computer.out)

    def test_less_than_function_positive(self):
        computer = main.Computer([1107, 4, 5, 5, 104, 77, 99], 0)
        computer.run()
        self.assertEqual(1, computer.out)

    def test_less_than_function_negative(self):
        computer = main.Computer([1107, 4, 4, 5, 104, 77, 99], 0)
        computer.run()
        self.assertEqual(0, computer.out)

    def test_equals_function_positive(self):
        computer = main.Computer([1108, 4, 4, 5, 104, 77, 99], 0)
        computer.run()
        self.assertEqual(1, computer.out)

    def test_equals_function_negative(self):
        computer = main.Computer([1108, 4, -4, 5, 104, 77, 99], 0)
        computer.run()
        self.assertEqual(0, computer.out)
