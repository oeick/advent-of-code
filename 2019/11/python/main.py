from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import NamedTuple

from computer import Computer


class Position(NamedTuple):
    x: int
    y: int


class Direction(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4

    def turn_left(self) -> Direction:
        return {Direction.NORTH: Direction.WEST,
                Direction.WEST: Direction.SOUTH,
                Direction.SOUTH: Direction.EAST,
                Direction.EAST: Direction.NORTH}[self]

    def turn_right(self) -> Direction:
        return {Direction.NORTH: Direction.EAST,
                Direction.EAST: Direction.SOUTH,
                Direction.SOUTH: Direction.WEST,
                Direction.WEST: Direction.NORTH}[self]

    def turn(self, direction_code: int) -> Direction:
        if direction_code == 0:
            return self.turn_left()
        elif direction_code == 1:
            return self.turn_right()
        else:
            raise ValueError(f'unknown direction code {direction_code}')


@dataclass
class Robot:
    position: Position
    direction: Direction

    def move(self):
        match self.direction:
            case Direction.NORTH:
                self.position = Position(self.position.x, self.position.y - 1)
            case Direction.EAST:
                self.position = Position(self.position.x + 1, self.position.y)
            case Direction.SOUTH:
                self.position = Position(self.position.x, self.position.y + 1)
            case Direction.WEST:
                self.position = Position(self.position.x - 1, self.position.y)


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        integers = {n: int(d) for n, d in enumerate(fp.read().split(','))}
    number_of_painted_panels = len(paint(integers, start_color=0))
    registration_identifier = draw_panels(paint(integers, start_color=1))
    return number_of_painted_panels, registration_identifier


def paint(program: dict[int, int], start_color: int) -> (int, str):
    comp = Computer(program, [])
    panels: dict[Position, int] = {Position(0, 0): start_color}
    outputs, out = [], 0
    robot = Robot(Position(0, 0), Direction.NORTH)
    while out is not None:
        comp.inp = [panels[robot.position], ]
        if (out := comp.run()) is not None:
            outputs.append(out)
            if len(outputs) == 2:
                handle_outputs(robot, panels, *outputs)
                outputs = []
    return panels


def handle_outputs(
        robot: Robot,
        panels: dict[Position, int],
        color: int,
        direction_code: int):
    panels[robot.position] = color
    robot.direction = robot.direction.turn(direction_code)
    robot.move()
    if robot.position not in panels:
        panels[robot.position] = 0


def draw_panels(panels: dict[Position, int]):
    xs = [p.x for p in panels.keys()]
    ys = [p.y for p in panels.keys()]
    x_min, x_max = min(xs), max(xs)
    y_min, y_max = min(ys), max(ys)
    rows = [['.'] * (x_max - x_min + 1) for _ in range(y_max - y_min + 1)]
    for panel, color in panels.items():
        col = panel.x - x_min
        row = panel.y - y_min
        rows[row][col] = '#' if color == 1 else '.'
    return '\n'.join([''.join(r) for r in rows])


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
