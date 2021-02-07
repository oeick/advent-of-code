import unittest
import main


class ExampleTests(unittest.TestCase):

    def test_example(self):
        example = """
        123 -> x
        456 -> y
        x AND y -> d
        x OR y -> e
        x LSHIFT 2 -> f
        y RSHIFT 2 -> g
        NOT x -> h
        NOT y -> i
        """
        lines = [line.strip() for line in example.splitlines() if line.strip()]
        instructions = main.parse_instructions(lines)
        wires = main.solve(instructions)
        expected = {
            'd': 72,
            'e': 507,
            'f': 492,
            'g': 114,
            'h': 65412,
            'i': 65079,
            'x': 123,
            'y': 456,
        }
        self.assertEqual(expected, wires)
