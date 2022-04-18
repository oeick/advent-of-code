import unittest
import main


class ExampleTests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(
            (1, 10),
            main.solve([
                "b inc 5 if a > 1",
                "a inc 1 if b < 5",
                "c dec -10 if a >= 1",
                "c inc -20 if c == 10"]))

    def test_parse_instruction(self):
        self.assertEqual(
            ('abc',
             'xyz',
             'abc + 1 if xyz > 9 else abc'),
            main.parse('abc inc 1 if xyz > 9'))
