import unittest
import main


class ExampleTests(unittest.TestCase):

    def test_part_1_example(self):
        example = r"""
        ""
        "abc"
        "aaa\"aaa"
        "\x27"
        """
        lines = [line.strip() for line in example.splitlines() if line.strip()]
        self.assertEqual(12, main.solve_part_1(lines))

    def test_part_2_example(self):
        example = r"""
        ""
        "abc"
        "aaa\"aaa"
        "\x27"
        """
        lines = [line.strip() for line in example.splitlines() if line.strip()]
        self.assertEqual(19, main.solve_part_2(lines))