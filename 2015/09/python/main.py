import re
from itertools import permutations

PATTERN = re.compile(r'(\w*) to (\w*) = (\d*)')


def calc_route_dist(distances, route: tuple) -> int:
    return sum(distances[route[i]][route[i+1]] for i in range(len(route)-1))


def parse_distances(lines: list[str]) -> dict[str, dict[str, int]]:
    distances = {}
    for line in lines:
        match = re.match(PATTERN, line)
        loc1, loc2, dist = match.groups()
        if loc1 in distances:
            distances[loc1][loc2] = int(dist)
        else:
            distances[loc1] = {loc2: int(dist)}
        if loc2 in distances:
            distances[loc2][loc1] = int(dist)
        else:
            distances[loc2] = {loc1: int(dist)}
    return distances


def solve(distances: dict[str, dict[str, int]]) -> (int, int):
    locations = set(distances.keys())
    routes = list(permutations(locations))
    route_distances = [(calc_route_dist(distances, r), r) for r in routes]
    shortest = min(route_distances)[0]
    longest = max(route_distances)[0]
    return shortest, longest


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        lines = fp.readlines()
    distances = parse_distances(lines)
    return solve(distances)


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
