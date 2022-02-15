from itertools import count
from typing import Iterator


def find_stop_number(r: int) -> int:
    return (2 * r + 1) ** 2


def find_rectangle_for(number: int) -> int:
    counter = count()
    while find_stop_number(n := next(counter)) < number:
        pass
    return n


def get_corner_numbers(r: int) -> list[int]:
    return [find_stop_number(r) - 2 * n * r for n in range(4)]


def find_location(number: int) -> tuple[int, int]:
    r = find_rectangle_for(number)
    southeast, southwest, northwest, northeast = get_corner_numbers(r)
    if number <= northeast:
        return r, number + r - northeast
    elif number <= northwest:
        return northwest - number - r, r
    elif number <= southwest:
        return -r, southwest - number - r
    else:
        return number + r - southeast, -r


def neighbors(x: int, y: int) -> Iterator[tuple[int, int]]:
    for neighbor in ((x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
                     (x - 1, y), (x + 1, y),
                     (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)):
        yield neighbor


def solve_part_1(square: int) -> int:
    x, y = find_location(square)
    return abs(x) + abs(y)


def solve_part_2(square: int) -> int:
    prior_sums = {(0, 0): 1}
    number = 2
    current_sum = 1
    while current_sum <= square:
        x, y = find_location(number)
        current_sum = sum([prior_sums[n] for n in neighbors(x, y)
                           if n in prior_sums])
        prior_sums[(x, y)] = current_sum
        number += 1
    return current_sum


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        square = int(fp.read())
    return solve_part_1(square), solve_part_2(square)


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
