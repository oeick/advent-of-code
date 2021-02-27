import unittest
from main import parse_input_lines, calc_distance, Specs, solve
from parameterized import parameterized


class ExampleTests(unittest.TestCase):

    def test_parser(self):
        result = parse_input_lines([
            'Dancer can fly 27 km/s for 5 seconds, '
            'but then must rest for 132 seconds.',
            'Cupid can fly 22 km/s for 2 seconds, '
            'but then must rest for 41 seconds.'
        ])
        self.assertEqual(
            {'Dancer': (27, 5, 132),
             'Cupid': (22, 2, 41)},
            result)

    @parameterized.expand([
        # duration, comet's distance, dancer's distance
        (1, 14, 16),
        (10, 140, 160),
        (11, 140, 176),
        (12, 140, 176),
        (137, 140, 176),
        (1000, 1120, 1056)
    ])
    def test_example(self, duration, comets_dist, dances_dist):
        comet = Specs(14, 10, 127)
        dancer = Specs(16, 11, 162)

        self.assertEqual(comets_dist, calc_distance(duration, comet))
        self.assertEqual(dances_dist, calc_distance(duration, dancer))
