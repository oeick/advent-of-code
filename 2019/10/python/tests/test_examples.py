import unittest

import main
from main import Target


class ExampleTests(unittest.TestCase):

    def test_get_coordinates(self):
        input_lines = ['.#..#',
                       '.....',
                       '#####',
                       '....#',
                       '...##']
        coords = main.get_coordinates(input_lines)
        self.assertEqual(
            [(0, 2), (1, 0), (1, 2), (2, 2), (3, 2),
             (3, 4), (4, 0), (4, 2), (4, 3), (4, 4)],
            coords)

    def test_get_detections(self):
        detections_from_example = main.get_detections(
            [(0, 2), (1, 0), (1, 2), (2, 2), (3, 2),
             (3, 4), (4, 0), (4, 2), (4, 3), (4, 4)])
        detection_counts = [len(d) for d in detections_from_example]
        self.assertEqual([6, 7, 7, 7, 7, 8, 7, 5, 7, 7], detection_counts)

    def test_part_1_larger_example_1(self):
        coordinates = main.get_coordinates(
            """......#.#.
               #..#.#....
               ..#######.
               .#.#.###..
               .#..#.....
               ..#....#.#
               #..#....#.
               .##.#..###
               ##...#..#.
               .#....####""".replace(' ', '').splitlines())
        self.assertEqual(
            ((5, 8), 33),
            main.get_part1_solution(coordinates))

    def test_part_1_larger_example_2(self):
        coordinates = main.get_coordinates(
            """#.#...#.#.
               .###....#.
               .#....#...
               ##.#.#.#.#
               ....#.#.#.
               .##..###.#
               ..#...##..
               ..##....##
               ......#...
               .####.###.""".replace(' ', '').splitlines())
        self.assertEqual(
            ((1, 2), 35),
            main.get_part1_solution(coordinates))

    def test_part_1_larger_example_3(self):
        coordinates = main.get_coordinates(
            """.#..#..###
               ####.###.#
               ....###.#.
               ..###.##.#
               ##.##.#.#.
               ....###..#
               ..#.#..#.#
               #..#.#.###
               .##...##.#
               .....#.#..""".replace(' ', '').splitlines())
        self.assertEqual(
            ((6, 3), 41),
            main.get_part1_solution(coordinates))

    def test_part_1_larger_example_4(self):
        coordinates = main.get_coordinates(
            """.#..##.###...#######
               ##.############..##.
               .#.######.########.#
               .###.#######.####.#.
               #####.##.#.##.###.##
               ..#####..#.#########
               ####################
               #.####....###.#.#.##
               ##.#################
               #####.##.###..####..
               ..######..##.#######
               ####.##.####...##..#
               .#####..#.######.###
               ##...#.##########...
               #.##########.#######
               .####.#.###.###.#.##
               ....##.##.###..#####
               .#.#.###########.###
               #.#.#.#####.####.###
               ###.##.####.##.#..##""".replace(' ', '').splitlines())
        self.assertEqual(
            ((11, 13), 210),
            main.get_part1_solution(coordinates))

    def test_sort_asteroids_for_laser(self):
        laser = (3, 3)
        coordinates = [(6, 6), (5, 5), (6, 0), (3, 2), (3, 1), (3, 0)]
        asteroids = main.sort_asteroids_for_laser(laser, coordinates)
        self.assertEqual(asteroids, [
            Target((3, 2), -180.0, 1, None),
            Target((3, 1), -180.0, 4, None),
            Target((3, 0), -180.0, 9, None),
            Target((6, 0), -135.0, 18, None),
            Target((5, 5), -45.0, 8, None),
            Target((6, 6), -45.0, 18, None)])

    def test_destroy_one_round(self):
        laser = (3, 3)
        coordinates = [(6, 6), (5, 5), (6, 0), (3, 2), (3, 1), (3, 0)]
        asteroids = main.sort_asteroids_for_laser(laser, coordinates)
        result = main.destroy_one_round(asteroids)
        self.assertEqual(result, [
            Target(coords=(3, 2), angle=-180.0, qdist=1, number=1),
            Target(coords=(3, 1), angle=-180.0, qdist=4, number=None),
            Target(coords=(3, 0), angle=-180.0, qdist=9, number=None),
            Target(coords=(6, 0), angle=-135.0, qdist=18, number=2),
            Target(coords=(5, 5), angle=-45.0, qdist=8, number=3),
            Target(coords=(6, 6), angle=-45.0, qdist=18, number=None)])

    def test_destroy_all_asteroids(self):
        laser = (3, 3)
        coordinates = [(6, 6), (5, 5), (6, 0), (3, 2), (3, 1), (3, 0)]
        asteroids = main.sort_asteroids_for_laser(laser, coordinates)
        result = main.destroy_all_asteroids(asteroids)
        self.assertEqual(result, [
            Target(coords=(3, 2), angle=-180.0, qdist=1, number=1),
            Target(coords=(3, 1), angle=-180.0, qdist=4, number=4),
            Target(coords=(3, 0), angle=-180.0, qdist=9, number=6),
            Target(coords=(6, 0), angle=-135.0, qdist=18, number=2),
            Target(coords=(5, 5), angle=-45.0, qdist=8, number=3),
            Target(coords=(6, 6), angle=-45.0, qdist=18, number=5)])

    def test_part_2_larger_example(self):
        coordinates = main.get_coordinates(
            """.#..##.###...#######
               ##.############..##.
               .#.######.########.#
               .###.#######.####.#.
               #####.##.#.##.###.##
               ..#####..#.#########
               ####################
               #.####....###.#.#.##
               ##.#################
               #####.##.###..####..
               ..######..##.#######
               ####.##.####...##..#
               .#####..#.######.###
               ##...#.##########...
               #.##########.#######
               .####.#.###.###.#.##
               ....##.##.###..#####
               .#.#.###########.###
               #.#.#.#####.####.###
               ###.##.####.##.#..##""".replace(' ', '').splitlines())
        laser = (11, 13)
        asteroids = main.sort_asteroids_for_laser(laser, coordinates)
        result = main.destroy_all_asteroids(asteroids)
        expected = {1: (11, 12),
                    2: (12, 1),
                    3: (12, 2),
                    10: (12, 8),
                    20: (16, 0),
                    50: (16, 9),
                    100: (10, 16),
                    199: (9, 6),
                    200: (8, 2),
                    201: (10, 9),
                    300: (11, 1)}
        for expected_number, expected_coords in expected.items():
            asteroid = [a for a in result if a.number == expected_number][0]
            self.assertEqual(asteroid.coords, expected_coords)
