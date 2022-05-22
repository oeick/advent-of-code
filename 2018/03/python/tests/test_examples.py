import unittest

import main


class ExampleTests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(
            (4, '3'),
            main.solve(main.parse_claims([
                "#1 @ 1,3: 4x4",
                "#2 @ 3,1: 4x4",
                "#3 @ 5,5: 2x2"])))
