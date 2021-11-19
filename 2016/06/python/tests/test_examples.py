import unittest
import main


class ExampleTests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(('easter', 'advent'), main.solve([
            'eedadn',
            'drvtee',
            'eandsr',
            'raavrd',
            'atevrs',
            'tsrnev',
            'sdttsa',
            'rasrtv',
            'nssdts',
            'ntnada',
            'svetve',
            'tesnvt',
            'vntsnd',
            'vrdear',
            'dvrsen',
            'enarar',
        ]))
