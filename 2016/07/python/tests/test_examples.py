import unittest
import main


class ExampleTests(unittest.TestCase):

    def test_solve(self):
        self.assertEqual(
            2,
            main.solve([
                'abba[mnop]qrst',
                'abcd[bddb]xyyx',
                'aaaa[qwer]tyui',
                'ioxxoj[asdfgh]zxcvbn']))
