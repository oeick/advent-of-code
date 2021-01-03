import unittest
import main


class ExampleTests(unittest.TestCase):

    def test_example(self):
        example = """..##.......
                     #...#...#..
                     .#....#..#.
                     ..#.#...#.#
                     .#...##..#.
                     ..#.##.....
                     .#.#.#....#
                     .#........#
                     #.##...#...
                     #...##....#
                     .#..#...#.#"""
        lines = [line.strip() for line in example.splitlines()]
        result1 = main.solve(lines, [(3, 1)])
        result2 = main.solve(lines, [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)])
        self.assertEqual(result1, 7)
        self.assertEqual(result2, 336)
