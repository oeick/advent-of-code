import unittest

from parameterized import parameterized

from main import Specs, parse_input_lines, calc_distance, calc_points


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

    @parameterized.expand([
        # duration, comet's points, dancer's points
        (139, 0, 139),
        (140, 1, 139),
        (1000, 312, 689)
    ])
    def test_part_2(self, duration, comets_points, dancers_points):
        example = {
            'comet': Specs(14, 10, 127),
            'dancer': Specs(16, 11, 162)}

        self.assertEqual(
            {'comet': comets_points,
             'dancer': dancers_points},
            calc_points(duration, example))
