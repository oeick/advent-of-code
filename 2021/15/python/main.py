from __future__ import annotations

from typing import NamedTuple, Optional, Iterator


class Chiton(NamedTuple):
    x: int
    y: int
    risk: int


class Step(NamedTuple):
    chiton: Chiton
    prev: Optional[Step]
    went: int
    dist: int

    def cost(self) -> int:
        return self.chiton.risk + self.went + self.dist


class Solver:
    cave: list[list[int]]
    x_max: int
    y_max: int

    def __init__(self, cave: list[list[int]]):
        self.cave = cave
        self.x_max = len(cave[0]) - 1
        self.y_max = len(cave) - 1

    def dist(self, chiton: Chiton) -> int:
        return self.x_max - chiton.x + self.y_max - chiton.y

    def neighbor_chitons(self, chiton: Chiton) -> Iterator[Chiton]:
        for x, y in ((chiton.x - 1, chiton.y), (chiton.x + 1, chiton.y),
                     (chiton.x, chiton.y - 1), (chiton.x, chiton.y + 1)):
            if 0 <= x <= self.x_max and 0 <= y <= self.y_max:
                yield Chiton(x, y, self.cave[y][x])

    def solve(self) -> int:
        # TODO: method to large
        first_chiton = Chiton(0, 0, self.cave[0][0])
        first_step = Step(chiton=first_chiton,
                          prev=None,
                          went=0,
                          dist=self.dist(first_chiton))
        last_chiton = Chiton(self.x_max, self.y_max, self.cave[-1][-1])
        open_steps: dict[Chiton, Step] = {first_step.chiton: first_step}
        closed_chitons: set[Chiton] = set()
        while last_chiton not in closed_chitons:
            # TODO: performance
            current_step = min(open_steps.items(), key=lambda i: i[1].cost())[1]
            del (open_steps[current_step.chiton])
            closed_chitons.add(current_step.chiton)
            for neighbor_chiton in self.neighbor_chitons(current_step.chiton):
                if neighbor_chiton in closed_chitons or (
                        neighbor_chiton in open_steps
                        and current_step.went + current_step.chiton.risk
                        >= open_steps[neighbor_chiton].went):
                    continue
                open_steps[neighbor_chiton] = Step(
                    chiton=neighbor_chiton,
                    prev=current_step,
                    went=current_step.went + current_step.chiton.risk,
                    dist=self.dist(neighbor_chiton))

        return current_step.went + current_step.chiton.risk - self.cave[0][0]


def quintuple_width(cave: list[list[int]]) -> list[list[int]]:
    x_size = len(cave[0])
    new_cave = []
    for row in cave:
        new_row = list(row)
        for _ in range(4):
            new_row += [n + 1 if n + 1 < 10 else 1 for n in new_row[-x_size:]]
        new_cave.append(new_row)
    return new_cave


def quintuple_cave(cave: list[list[int]]) -> list[list[int]]:
    y_size = len(cave)
    big_cave = list(quintuple_width(cave))
    for j in range(4):
        for i in range(y_size):
            big_cave.append([n + 1 if n + 1 < 10 else 1
                             for n in big_cave[j * y_size + i]])
    return big_cave


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        lines = fp.read().splitlines()
    cave = [[int(c) for c in line] for line in lines]
    return Solver(cave).solve(), Solver(quintuple_cave(cave)).solve()


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
