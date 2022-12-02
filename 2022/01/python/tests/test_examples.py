import unittest
import main


class ExampleTests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(
            (24000, 45000),
            main.solve(['1000',
                        '2000',
                        '3000',
                        '',
                        '4000',
                        '',
                        '5000',
                        '6000',
                        '',
                        '7000',
                        '8000',
                        '9000',
                        '',
                        '10000']))
