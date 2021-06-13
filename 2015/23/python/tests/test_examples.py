import unittest

import main


class ExampleTests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(
            {"a": 2, "b": 0},
            main.process_instructions(
                instructions=[
                    "inc a",
                    "jio a, +2",
                    "tpl a",
                    "inc a"],
                start_values={"a": 0, "b": 0})
        )
