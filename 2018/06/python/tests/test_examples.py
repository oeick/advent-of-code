import unittest

import main
from main import Coords


class MainTests(unittest.TestCase):

    def test_coords_dist(self):
        self.assertEqual(3, Coords(1, 2).dist(Coords(2, 0)))

    def test_parse_coords(self):
        self.assertEqual(
            [Coords(1, 2), Coords(2, 0)],
            main.parse_coordinates(["1,2", "2,0"]))

    def test_bounding_rectangle(self):
        self.assertEqual(
            (Coords(1, 2), Coords(5, 4)),
            main.bounding_rectangle([
                Coords(3, 2), Coords(3, 4), Coords(1, 3), Coords(5, 2)]))

    def test_generate_edge_coordinates(self):
        self.assertEqual(
            {Coords(1, 2), Coords(2, 2), Coords(3, 2),
             Coords(1, 3), Coords(3, 3),
             Coords(1, 4), Coords(2, 4), Coords(3, 4)},
            main.generate_edge_coordinates((Coords(1, 2), Coords(3, 4))))

    def test_find_size_of_largest_area(self):
        self.assertEqual(
            17,
            main.find_size_of_largest_area([Coords(1, 1),
                                            Coords(1, 6),
                                            Coords(8, 3),
                                            Coords(3, 4),
                                            Coords(5, 5),
                                            Coords(8, 9)]))

    def test_find_size_of_save_region(self):
        self.assertEqual(
            16,
            main.find_size_of_save_region([Coords(1, 1),
                                           Coords(1, 6),
                                           Coords(8, 3),
                                           Coords(3, 4),
                                           Coords(5, 5),
                                           Coords(8, 9)], 32))
