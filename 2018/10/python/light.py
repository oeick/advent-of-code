import re
from dataclasses import dataclass
from typing import Self

PATTERN = re.compile(
    r'position=<\s*(-?\d+),\s*(-?\d+)> velocity=<\s*(-?\d+),\s*(-?\d+)>')


@dataclass
class Light:
    position: tuple[int, int]
    velocity: tuple[int, int]

    @staticmethod
    def parse(input_line: str) -> Self:
        matcher = re.match(PATTERN, input_line)
        x, y, vx, vy = [int(m) for m in matcher.groups()]
        return Light((x, y), (vx, vy))

    def move(self):
        self.position = (self.position[0] + self.velocity[0],
                         self.position[1] + self.velocity[1])
