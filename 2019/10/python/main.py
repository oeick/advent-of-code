from dataclasses import dataclass
from math import degrees, atan2
from typing import Optional


@dataclass
class Target:
    coords: tuple[int, int]
    angle: float
    qdist: int
    number: Optional[int]


COORDS = list[tuple[int, int]]


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        lines = fp.read().splitlines()
    return solve(lines)


def solve(lines: list[str]) -> (int, int):
    coordinates = get_coordinates(lines)
    station, detections = get_part1_solution(coordinates)
    asteroids = sort_asteroids_for_laser(station, coordinates)
    result = destroy_all_asteroids(asteroids)
    asteroid_200 = [a for a in result if a.number == 200][0]
    return detections, asteroid_200.coords[0] * 100 + asteroid_200.coords[1]


def get_coordinates(inputlines: list[str]) -> COORDS:
    """
    >>> get_coordinates(['.#..', '#...', '...#'])
    [(0, 1), (1, 0), (3, 2)]
    """
    return [(x, y)
            for x in range(len(inputlines[0]))
            for y in range(len(inputlines))
            if inputlines[y][x] == '#']


def get_part1_solution(coordinates: COORDS) -> ((int, int), int):
    detections = get_detections(coordinates)
    detection_counts = [len(d) for d in detections]
    i_max_detections = detection_counts.index(max(detection_counts))
    return coordinates[i_max_detections], detection_counts[i_max_detections]


def get_detections(coordinates: COORDS) -> list[list[int]]:
    """
    >>> get_detections([(0, 0), (1, 1), (2, 2)])
    [[1], [0, 2], [1]]
    >>> get_detections([(0, 2), (1, 0), (1, 2)])
    [[1, 2], [0, 2], [0, 1]]
    """
    detections = []
    for coord0 in coordinates:
        local_detections = []
        angles = calc_angles(coord0, coordinates)
        qdists = calc_qdists(coord0, coordinates)
        for i1, coord1 in enumerate(coordinates):
            if coord1 == coord0:
                continue
            visible = True
            for i2, coord2 in enumerate(coordinates):
                if coord2 in (coord0, coord1):
                    continue
                if angles[i1] == angles[i2] and qdists[i1] > qdists[i2]:
                    visible = False
                    break
            if visible:
                local_detections.append(i1)
            else:
                continue
        detections.append(local_detections)
    return detections


def calc_angles(start: (int, int), targets: COORDS) -> list[float]:
    """
    >>> calc_angles((1, 1), [(1, 0), (2, 0), (3, 1)])
    [-180.0, -135.0, -90.0]
    >>> calc_angles((1, 1), [(0, 1), (1, 2), (3, 3)])
    [90.0, 0.0, -45.0]
    >>> calc_angles((1, 1), [(1, 1)])
    [0.0]
    """
    angles = [degrees(atan2(start[0] - x, y - start[1])) for x, y in targets]
    return [-a if a == 180.0 else a for a in angles]


def calc_qdists(start: (int, int), targets: COORDS) -> list[int]:
    """
    >>> calc_qdists((1, 1), [(1, 0), (2, 0), (3, 1)])
    [1, 2, 4]
    >>> calc_qdists((1, 1), [(0, 1), (1, 2), (3, 3)])
    [1, 1, 8]
    >>> calc_qdists((1, 1), [(1, 1)])
    [0]
    """
    return [(x - start[0]) ** 2 + (y - start[1]) ** 2 for x, y in targets]


def sort_asteroids_for_laser(
        laser: tuple[int, int], coordinates: COORDS) -> list[Target]:
    angles = calc_angles(laser, coordinates)
    qdists = calc_qdists(laser, coordinates)
    unsorted_asteroids = [Target(c, angles[i], qdists[i], None)
                          for i, c in enumerate(coordinates)]
    asteroids = sorted(unsorted_asteroids, key=lambda a: (a.angle, a.qdist))
    return asteroids


def destroy_all_asteroids(asteroids: list[Target]) -> list[Target]:
    while [a for a in asteroids if a.number is None]:
        asteroids = destroy_one_round(asteroids)
    return asteroids


def destroy_one_round(asteroids: list[Target]) -> list[Target]:
    next_number = max(
        asteroids,
        key=lambda a: a.number if a.number is not None else -1).number
    next_number = next_number + 1 if next_number is not None else 1
    i = 0
    while i < len(asteroids):
        if asteroids[i].number is None:
            asteroids[i].number = next_number
            next_number += 1
            j = i + 1
            while j < len(asteroids) \
                    and asteroids[j].angle == asteroids[i].angle:
                j += 1
            i = j
        else:
            i += 1
    return asteroids


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
