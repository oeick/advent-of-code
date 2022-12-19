from __future__ import annotations

import operator
from dataclasses import dataclass
from typing import Self, Callable


@dataclass
class Monkey:
    items: list[int]
    operation: operator
    divisor: int
    targets: dict[bool, int]
    inspections: int

    def test(self, item: int) -> bool:
        return item % self.divisor == 0

    def clone(self) -> Self:
        return Monkey(list(self.items),
                      self.operation,
                      self.divisor,
                      self.targets,
                      self.inspections)

    @staticmethod
    def of(lines: list[str]) -> Monkey:
        divisor = int(lines[3].rsplit(' ', 1)[-1])
        return Monkey(
            [int(v) for v in lines[1].rsplit(':', 1)[1].split(', ')],
            Monkey.parse_operation(lines[2]),
            divisor,
            Monkey.parse_targets(lines[4:6]),
            0)

    @staticmethod
    def parse_targets(lines: list[str]) -> dict[bool, int]:
        return {True: int(lines[0].rsplit(' ', 1)[-1]),
                False: int(lines[1].rsplit(' ', 1)[-1])}

    @staticmethod
    def parse_operation(line: str) -> Callable:
        op, value = line.rsplit(' ', 2)[1:3]
        operation = operator.mul if op == '*' else operator.add
        return lambda x: operation(x, x if value == 'old' else int(value))
