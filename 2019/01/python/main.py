def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        masses = [int(r) for r in fp]
    return solve_part_1(masses), solve_part_2(masses)


def solve_part_1(masses: list[int]) -> int:
    return sum(calc_partial_fuel(m) for m in masses)


def solve_part_2(masses: list[int]) -> int:
    return sum(calc_total_fuel(m) for m in masses)


def calc_partial_fuel(mass: int) -> int:
    return mass // 3 - 2


def calc_total_fuel(mass: int) -> int:
    if mass >= 9:
        fuel = calc_partial_fuel(mass)
        fuel += calc_total_fuel(fuel)
    else:
        fuel = 0
    return fuel


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
