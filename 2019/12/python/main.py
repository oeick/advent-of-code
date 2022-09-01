import re
from re import Pattern

from moon import Moon


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        lines = fp.read().splitlines()
    positions = parse_positions(lines)
    return solve_part_1(positions), solve_part_2(positions)


def solve_part_1(positions: list[list[int]]) -> int:
    moons = [Moon(n, list(positions[i]))
             for i, n in enumerate(('Io', 'Europa', 'Ganymede', 'Callisto'))]
    moons = simulate_moons(moons, steps=1000)
    return calc_total_energy(moons)


def solve_part_2(positions: list[list[int]]) -> int:
    nx = get_period([p[0] for p in positions])
    ny = get_period([p[1] for p in positions])
    nz = get_period([p[2] for p in positions])
    return nx * ny * nz


def parse_positions(lines: list[str]) -> list[list[int]]:
    pattern = re.compile(r'<x=(.*), y=(.*), z=(.*)>')
    return [parse_position_from_line(line, pattern) for line in lines]


def parse_position_from_line(line: str, pattern: Pattern) -> list[int]:
    return [int(n) for n in pattern.match(line).groups()]


def simulate_moons(moons: list[Moon], steps: int) -> list[Moon]:
    for _ in range(steps):
        moons = step_moons(moons)
    return moons


def step_moons(moons: list[Moon]) -> list[Moon]:
    moons = update_velocity(moons)
    moons = update_position(moons)
    return moons


def update_velocity(moons: list[Moon]) -> list[Moon]:
    for moon in moons:
        for other in moons:
            moon.add_vel(other)
    return moons


def update_position(moons: list[Moon]) -> list[Moon]:
    for moon in moons:
        moon.move()
    return moons


def calc_total_energy(moons: list[Moon]) -> int:
    return sum([m.kin() * m.pot() for m in moons])


def get_period(pos: list[int]) -> int:
    vel = [0, 0, 0, 0]
    n = 0
    while n == 0 or vel != [0, 0, 0, 0]:
        a = [sum(1 for q in pos if q > p) - sum(1 for q in pos if q < p)
             for p in pos]
        vel = [v + a[i] for i, v in enumerate(vel)]
        pos = [p + vel[i] for i, p in enumerate(pos)]
        n += 1
    return n


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
