import unittest

import main
from main import Line, Point


class ExampleTests(unittest.TestCase):

    def test_parse_text(self):
        self.assertEqual(
            (Point(0, 9), Point(5, 9)),
            main.parse_text('0,9 -> 5,9'))

    def test_get_number_of_overlaps(self):
        self.assertEqual(
            5,
            main.get_number_of_overlaps([
                Line(Point(0, 9), Point(5, 9)),
                Line(Point(9, 4), Point(3, 4)),
                Line(Point(2, 2), Point(2, 1)),
                Line(Point(7, 0), Point(7, 4)),
                Line(Point(0, 9), Point(2, 9)),
                Line(Point(3, 4), Point(1, 4))]))

    def test_get_line_points(self):
        self.assertEqual(
            [Point(2, 3), Point(3, 3), Point(4, 3)],
            main.get_line_points(Line(Point(2, 3), Point(4, 3))))
        self.assertEqual(
            [Point(2, 3), Point(2, 4), Point(2, 5)],
            main.get_line_points(Line(Point(2, 3), Point(2, 5))))

    def test_put_points_into_map(self):
        #  |0123456
        # -+-------
        # 0|   1
        # 1|   1
        # 2| 123211
        # 3|   1
        point_map = {}
        main.put_points_into_map(Line(Point(3, 0), Point(3, 3)), point_map)
        main.put_points_into_map(Line(Point(1, 2), Point(6, 2)), point_map)
        main.put_points_into_map(Line(Point(2, 2), Point(4, 2)), point_map)
        self.assertEqual(
            {Point(3, 0): 1,
             Point(3, 1): 1,
             Point(1, 2): 1,
             Point(2, 2): 2,
             Point(3, 2): 3,
             Point(4, 2): 2,
             Point(5, 2): 1,
             Point(6, 2): 1,
             Point(3, 3): 1},
            point_map)

    def test_get_line_points_diagonal(self):
        self.assertEqual(
            [Point(1, 2), Point(2, 3), Point(3, 4)],
            main.get_line_points(Line(Point(1, 2), Point(3, 4))))
        self.assertEqual(
            [Point(6, 2), Point(5, 3), Point(4, 4)],
            main.get_line_points(Line(Point(6, 2), Point(4, 4))))
