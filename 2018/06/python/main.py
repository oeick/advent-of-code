from __future__ import annotations

from itertools import product
from typing import NamedTuple


class Coords(NamedTuple):
    x: int
    y: int

    def dist(self, other: Coords) -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)


def main(filename: str) -> tuple[int, int]:
    with open(filename, 'r') as fp:
        lines = fp.read().splitlines()
    coordinates = parse_coordinates(lines)
    return solve(coordinates)


def parse_coordinates(lines: list[str]) -> list[Coords]:
    tokens = [line.split(',') for line in lines]
    return [Coords(int(x), int(y)) for x, y in tokens]


def solve(coordinates: list[Coords]) -> tuple[int, int]:
    return (find_size_of_largest_area(coordinates),
            find_size_of_save_region(coordinates, 10_000))


def find_size_of_save_region(coordinates: list[Coords], dist_limit: int) -> int:
    return len(find_coords_with_limited_total_distance(coordinates, dist_limit))


def find_size_of_largest_area(coordinates: list[Coords]) -> int:
    unique_closest_coords = generate_map_of_unique_closest_coords(coordinates)
    candidates = get_candidates(coordinates)
    candidate_with_largest_area = max(
        set(candidates), key=lambda c: unique_closest_coords.count(c))
    return unique_closest_coords.count(candidate_with_largest_area)


def get_candidates(coordinates: list[Coords]) -> list[Coords]:
    infinity_coords = calculate_closest_coordinates_on_edge(coordinates)
    candidates = [c for c in coordinates if c not in infinity_coords]
    return candidates


def calculate_closest_coordinates_on_edge(
        coordinates: list[Coords]) -> set[Coords]:
    bounding_rect = bounding_rectangle(coordinates)
    edge_coords = generate_edge_coordinates(bounding_rect)
    unique_coords = set()
    for coord_e in edge_coords:
        distances = calculate_distances(coord_e, coordinates)
        if distances.count(min(distances)) == 1:
            unique_coords.add(coordinates[distances.index(min(distances))])
    return unique_coords


def bounding_rectangle(coordinates: list[Coords]) -> tuple[Coords, Coords]:
    x_values = set(c.x for c in coordinates)
    y_values = set(c.y for c in coordinates)
    return (Coords(min(x_values), min(y_values)),
            Coords(max(x_values), max(y_values)))


def generate_edge_coordinates(rectangle: tuple[Coords, Coords]) -> set[Coords]:
    x1, y1 = rectangle[0]
    x2, y2 = rectangle[1]
    top = [Coords(x, y1) for x in range(x1, x2 + 1)]
    bottom = [Coords(x, y2) for x in range(x1, x2 + 1)]
    left = [Coords(x1, y) for y in range(y1, y2 + 1)]
    right = [Coords(x2, y) for y in range(y1, y2 + 1)]
    return set(top + bottom + left + right)


def calculate_distances(target: Coords, coordinates: list[Coords]) -> list[int]:
    return [target.dist(c) for c in coordinates]


def generate_map_of_unique_closest_coords(
        coordinates: list[Coords]) -> list[Coords]:
    bounds = bounding_rectangle(coordinates)
    all_closest = []
    for x, y in product(
            range(bounds[0][0], bounds[1][0] + 1),
            range(bounds[0][1], bounds[1][1] + 1)):
        distances = generate_distances_dict(Coords(x, y), coordinates)
        closest = [(c, distances[c]) for c in distances
                   if distances[c] == min(distances.values())]
        if len(closest) == 1:
            all_closest.append(closest[0][0])
    return all_closest


def generate_distances_dict(
        target: Coords, coordinates: list[Coords]) -> dict[Coords, int]:
    return {c: target.dist(c) for c in coordinates}


def find_coords_with_limited_total_distance(
        coordinates: list[Coords], dist_limit: int) -> set[Coords]:
    bounds = bounding_rectangle(coordinates)
    resulting_coordinates = set()
    for x, y in product(
            range(bounds[0].x, bounds[1].x + 1),
            range(bounds[0].y, bounds[1].y + 1)):
        sum_of_distances = sum([Coords(x, y).dist(c) for c in coordinates])
        if sum_of_distances < dist_limit:
            resulting_coordinates.add(Coords(x, y))
    return resulting_coordinates


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
