import math
from typing import Callable

from Monkey import Monkey


def main(filename: str) -> tuple[int, int]:
    with open(filename, 'r') as fp:
        lines = fp.read().splitlines()
    monkeys = parse_monkeys(lines)
    return (
        solve(monkeys,
              rounds=20,
              reducer=lambda w: w // 3),
        solve(monkeys,
              rounds=10_000,
              reducer=lambda w: w % multiply_divisors(monkeys)))


def parse_monkeys(lines: list[str]) -> dict[int, Monkey]:
    monkeys = {}
    for r in range(0, len(lines), 7):
        monkeys[r // 7] = Monkey.of(lines[r:r + 7])
    return monkeys


def multiply_divisors(monkeys: dict[int, Monkey]) -> int:
    return math.prod(m.divisor for m in monkeys.values())


def solve(monkeys: dict[int, Monkey], rounds: int, reducer: Callable) -> int:
    monkeys = {i: m.clone() for i, m in monkeys.items()}
    for _ in range(rounds):
        do_round(monkeys, reducer)
    inspected = sorted([m.inspections for m in monkeys.values()])
    return inspected[-1] * inspected[-2]


def do_round(monkeys: dict[int, Monkey], reducer: Callable) -> None:
    for i, monkey in monkeys.items():
        while monkey.items:
            old_item = monkey.items.pop(0)
            new_item = monkey.operation(old_item)
            worry = reducer(new_item)
            monkeys[monkey.targets[monkey.test(worry)]].items.append(worry)
            monkey.inspections += 1


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
