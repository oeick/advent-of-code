import unittest

import main


class ExampleTests(unittest.TestCase):

    def test_find_start_on_1st_keyboard(self):
        self.assertEqual(
            (1, 1),
            main.find_start(
                keyboard=[
                    "123",
                    "456",
                    "789",
                ],
                key="5"
            )
        )

    def test_find_start_on_2nd_keyboard(self):
        self.assertEqual(
            (2, 0),
            main.find_start(
                keyboard=[
                    "--1--",
                    "-234-",
                    "56789",
                    "-ABC-",
                    "--D--",
                ],
                key="5"
            )
        )

    def test_example_part_1(self):
        self.assertEqual(
            "1985",
            main.solve(
                keyboard=[
                    "123",
                    "456",
                    "789",
                ],
                instructions=[
                    "ULL",
                    "RRDDD",
                    "LURDL",
                    "UUUUD"
                ]
            ))

    def test_example_part_2(self):
        self.assertEqual(
            "5DB3",
            main.solve(
                keyboard=[
                    "--1--",
                    "-234-",
                    "56789",
                    "-ABC-",
                    "--D--",
                ],
                instructions=[
                    "ULL",
                    "RRDDD",
                    "LURDL",
                    "UUUUD"
                ]
            ))
