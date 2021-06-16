import math


def find_next_valid_bus(
        prev_hit: int, prev_period: int, new_dist: int, new_bus: int) -> int:
    """
    prev_hit: when the previous busses met the condition
    prev_period: period of the condition of the previous busses
    new_dist: how many minutes after the 1st bus the new bus must depart
    new_bus: id number of the new bus
    """
    minute = prev_hit
    while (minute + new_dist) % new_bus != 0:
        minute += prev_period
    return minute


def find_next_period(
        prev_hit: int,
        prev_period: int,
        new_dist: int,
        new_bus: int) -> (int, int):
    first_hit = find_next_valid_bus(prev_hit, prev_period, new_dist, new_bus)
    second_hit = find_next_valid_bus(
        first_hit + prev_period, prev_period, new_dist, new_bus)
    return first_hit, second_hit - first_hit


def solve_part_2(ids: str) -> int:
    busses = [(p, int(i)) for p, i in enumerate(ids.split(',')) if i != 'x']
    minute_hit, period_hit = 2, 1
    for dist, bus_id in busses:
        minute_hit, period_hit = find_next_period(
            minute_hit, period_hit, dist, bus_id)
    return minute_hit


def solve_part_1(eta: int, ids: str) -> int:
    known_ids = [int(d) for d in ids.split(',') if d != 'x']
    waiting_t = [math.ceil(eta / i) * i - eta for i in known_ids]

    shortest_waiting_time = min(waiting_t)
    next_bus = known_ids[waiting_t.index(shortest_waiting_time)]

    return next_bus * shortest_waiting_time


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        lines = fp.read().splitlines()
    eta, ids = int(lines[0]), lines[1]
    return solve_part_1(eta, ids), solve_part_2(ids)


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
