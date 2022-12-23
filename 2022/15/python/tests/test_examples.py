import unittest

from parameterized import parameterized

import main
from main import Coord, Sensor, Span

EXAMPLE = """
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
""".splitlines()[1:]


class ExampleTests(unittest.TestCase):

    def test_example_part_1(self):
        sensors = main.parse_sensors(EXAMPLE)
        self.assertEqual(26, main.solve_part_1(sensors, 10))

    def test_solve_part_1_1_no_coord(self):
        sensors = [Sensor(Coord(0, 0), Coord(0, 3))]
        self.assertEqual(0, main.solve_part_1(sensors, 4))

    def test_solve_part_1_1_one_coord(self):
        sensors = [Sensor(Coord(0, 0), Coord(3, 0))]
        self.assertEqual(1, main.solve_part_1(sensors, 3))

    def test_solve_part_1_sensor_on_same_row(self):
        sensors = [Sensor(Coord(0, 0), Coord(0, 2))]
        self.assertEqual(5, main.solve_part_1(sensors, 0))

    def test_solve_part_1_beacon_on_same_row(self):
        sensors = [Sensor(Coord(0, 2), Coord(0, 0))]
        self.assertEqual(0, main.solve_part_1(sensors, 0))

    def test_solve_part_1_separate_spans(self):
        sensors = [Sensor(Coord(1, 2), Coord(2, 4)),
                   Sensor(Coord(7, 1), Coord(7, 3))]
        self.assertEqual(6, main.solve_part_1(sensors, 0))

    def test_solve_part_1_joined_spans(self):
        sensors = [Sensor(Coord(3, 0), Coord(0, 2)),
                   Sensor(Coord(5, -2), Coord(6, 0))]
        self.assertEqual(5, main.solve_part_1(sensors, -4))

    @parameterized.expand([
        (False, Span(0, 2), Span(4, 6)),
        (True, Span(0, 3), Span(4, 6)),
        (True, Span(0, 4), Span(4, 6)),
        (True, Span(0, 5), Span(4, 6)),
        (True, Span(0, 6), Span(4, 6)),
        (True, Span(0, 7), Span(4, 6)),
        (True, Span(7, 7), Span(4, 6)),
        (False, Span(8, 9), Span(4, 6))])
    def test_span_touches(self, expected, span1, span2):
        self.assertEqual(expected, span1.touches(span2))

    def test_merge_first_overlap_2_to_1(self):
        self.assertEqual({Span(-2, 5)},
                         main.merge_first_overlap({
                             Span(-2, 1),
                             Span(0, 5)}))

    def test_merge_first_overlap_2_to_2(self):
        self.assertEqual({Span(-2, 1), Span(3, 5)},
                         main.merge_first_overlap({
                             Span(-2, 1),
                             Span(3, 5)}))

    def test_merge_all_overlaps_3_to_2(self):
        self.assertEqual({Span(-2, 0), Span(2, 9)},
                         main.merge_all_overlaps({
                             Span(-2, 0),
                             Span(2, 4),
                             Span(3, 9)}))

    def test_merge_all_overlaps_3_1(self):
        self.assertEqual({Span(-2, 9)},
                         main.merge_all_overlaps({
                             Span(-2, 0),
                             Span(1, 4),
                             Span(2, 9)}))

    def test_merge_all_overlaps_4_to_2(self):
        self.assertEqual({Span(-2, 2), Span(4, 9)},
                         main.merge_all_overlaps({
                             Span(-2, 0),
                             Span(0, 2),
                             Span(4, 6),
                             Span(5, 9)}))

    def test_example_part_2(self):
        sensors = main.parse_sensors(EXAMPLE)
        self.assertEqual(
            56000011,
            main.solve_part_2(sensors, 20)
        )
