import unittest

import main
from main import COORDS


class ExampleTests(unittest.TestCase):

    def test_parser(self):
        self.assertEqual(
            [['.', '.', '#'],
             ['#', '#', '.'],
             ['.', '.', '.']],
            main.parse_grid(['..#', '##.', '...']))

    def test_get_neighbor_candidates(self):
        self.assertEqual(
            [COORDS(x=-1, y=7), COORDS(x=-1, y=8), COORDS(x=-1, y=9),
             COORDS(x=0, y=7),                     COORDS(x=0, y=9),
             COORDS(x=1, y=7),  COORDS(x=1, y=8),  COORDS(x=1, y=9)],
            main.get_neighbor_candidates(COORDS(0, 8))
        )

    def test_get_neighbor_coords(self):
        self.assertEqual(
            [COORDS(x=0, y=1), COORDS(x=1, y=1), COORDS(x=1, y=2)],
            main.get_neighbor_coords(
                COORDS(0, 2),
                [['.', '.', '.'],
                 ['.', '.', '.'],
                 ['#', '.', '.']]
            )
        )

    def test_count_neighbors_example_1(self):
        example = main.parse_grid([
                    '###...',
                    '###...',
                    '......',
                    '..###.',
                    '..###.',
                    '..###.'])
        self.assertEqual(5, main.count_neighbors(main.COORDS(1, 0), example))
        self.assertEqual(8, main.count_neighbors(main.COORDS(3, 4), example))

    def test_calc_next_state(self):
        self.assertEqual(
            main.parse_grid([
                '..##..',
                '..##.#',
                '...##.',
                '......',
                '#.....',
                '#.##..']),
            main.calc_next_state(
                main.parse_grid([
                    '.#.#.#',
                    '...##.',
                    '#....#',
                    '..#...',
                    '#.#..#',
                    '####..']))
        )

    def test_calc_nth_state(self):
        self.assertEqual(main.parse_grid([
            '......',
            '......',
            '..##..',
            '..##..',
            '......',
            '......']),
            main.calc_nth_state(
                main.parse_grid([
                    '.#.#.#',
                    '...##.',
                    '#....#',
                    '..#...',
                    '#.#..#',
                    '####..']),
                n=4)
        )

    def test_count_lights(self):
        self.assertEqual(
            15,
            main.count_lights(main.parse_grid([
                '.#.#.#',
                '...##.',
                '#....#',
                '..#...',
                '#.#..#',
                '####..']))
        )

    def test_solve_part_1(self):
        self.assertEqual(
            4,
            main.solve_part_1(main.parse_grid([
                '.#.#.#',
                '...##.',
                '#....#',
                '..#...',
                '#.#..#',
                '####..']),
                steps=4)
        )

    def test_solve_part_2(self):
        self.assertEqual(
            main.parse_grid([
                '##.###',
                '.##..#',
                '.##...',
                '.##...',
                '#.#...',
                '##...#']),
            main.calc_nth_state(main.parse_grid([
                '##.#.#',
                '...##.',
                '#....#',
                '..#...',
                '#.#..#',
                '####.#']),
                n=5,
                stucked=[COORDS(0, 0),
                         COORDS(0, 5),
                         COORDS(5, 5,),
                         COORDS(5, 0)])
        )
