import unittest
import main


class ExampleTests(unittest.TestCase):

    def test_validate(self):
        self.assertTrue(main.validate((2, 4, 3)))
        self.assertFalse(main.validate((5, 10, 25)))

    def test_solve_part_1(self):
        self.assertEqual(
            2,
            main.solve_part_1(
                [(2, 4, 3),
                 (1, 9, 1),
                 (7, 6, 5)]
            )
        )

    def test_solve_part_2(self):
        self.assertEqual(
            6,
            main.solve_part_2([
                (101, 301, 501),
                (102, 302, 502),
                (103, 303, 503),
                (201, 401, 601),
                (202, 402, 602),
                (203, 403, 603),
            ]))
