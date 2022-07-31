import unittest
import main
from main import Coords
from parameterized import parameterized


def parse_wires(wire1s: str, wire2s: str) -> tuple[list[Coords], list[Coords]]:
    wire1 = main.calc_wire_coords(main.parse_wire_path(wire1s))
    wire2 = main.calc_wire_coords(main.parse_wire_path(wire2s))
    return wire1, wire2


def parse_intersections(wire1s: str, wire2s: str) -> set[Coords]:
    wire1, wire2 = parse_wires(wire1s, wire2s)
    return set(wire1).intersection(set(wire2))


class ExampleTests(unittest.TestCase):

    def test_parse_first_wire(self):
        self.assertEqual(
            [('R', 8), ('U', 5), ('L', 5), ('D', 3)],
            main.parse_wire_path("R8,U5,L5,D3"))

    def test_parse_second_wire(self):
        self.assertEqual(
            [('U', 7), ('R', 6), ('D', 4), ('L', 4)],
            main.parse_wire_path("U7,R6,D4,L4"))

    @parameterized.expand([
        (6, ("R8,U5,L5,D3",
             "U7,R6,D4,L4")),
        (159, ("R75,D30,R83,U83,L12,D49,R71,U7,L72",
               "U62,R66,U55,R34,D71,R55,D58,R83")),
        (135, ("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
               "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"))])
    def test_solve_part_1(self, expected, wires):
        self.assertEqual(
            expected,
            main.solve_part_1(parse_intersections(*wires)))

    @parameterized.expand([
        (30, ("R8,U5,L5,D3",
              "U7,R6,D4,L4")),
        (610, ("R75,D30,R83,U83,L12,D49,R71,U7,L72",
               "U62,R66,U55,R34,D71,R55,D58,R83")),
        (410, ("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
               "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"))])
    def test_solve_part_2(self, expected, wires):
        wire1, wire2 = parse_wires(*wires)
        self.assertEqual(
            expected,
            main.solve_part_2(wire1, wire2, parse_intersections(*wires)))
