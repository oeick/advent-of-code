from __future__ import annotations
from dataclasses import dataclass, field


def get_default_velocity() -> list[int]:
    return [0, 0, 0]


@dataclass
class Moon:
    name: str
    pos: list[int]
    vel: list[int] = field(default_factory=get_default_velocity)

    def add_vel(self, other: Moon):
        for i in range(3):
            if other.pos[i] > self.pos[i]:
                self.vel[i] += 1
            elif other.pos[i] < self.pos[i]:
                self.vel[i] -= 1

    def move(self):
        for i in range(3):
            self.pos[i] += self.vel[i]

    def kin(self) -> int:
        return sum([abs(v) for v in self.vel])

    def pot(self) -> int:
        return sum([abs(p) for p in self.pos])

    def clone(self) -> Moon:
        return Moon(self.name, list(self.pos), list(self.vel))
