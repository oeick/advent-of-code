import re
from itertools import combinations
from typing import NamedTuple, Self

PATTERN = re.compile(r'.+ x=(-?\d+), y=(-?\d+): .+ x=(-?\d+), y=(-?\d+)')


class Coord(NamedTuple):
    x: int
    y: int

    def distance(self, other: Self) -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)


class Sensor(NamedTuple):
    pos: Coord
    beacon: Coord


class Span(NamedTuple):
    left: int
    right: int

    def touches(self, other: Self) -> bool:
        return self.right >= other.left - 1 and self.left <= other.right + 1

    def join(self, other: Self) -> Self:
        return Span(min(self.left, other.left),
                    max(self.right, other.right))

    def includes(self, x: int) -> bool:
        return self.left <= x <= self.right

    def __len__(self) -> int:
        return self.right - self.left + 1


def main(filename: str) -> tuple[int, int]:
    with open(filename, 'r') as fp:
        lines = fp.read().splitlines()
    sensors = parse_sensors(lines)
    return (
        solve_part_1(sensors, 2_000_000),
        solve_part_2(sensors, 4_000_000))


def parse_sensors(lines: list[str]) -> list[Sensor]:
    sensors = []
    for line in lines:
        match = PATTERN.match(line)
        xs, ys, xb, yb = [int(v) for v in match.groups()[0:4]]
        sensors.append(Sensor(Coord(xs, ys), Coord(xb, yb)))
    return sensors


def solve_part_1(sensors: list[Sensor], y: int) -> int:
    exclusion_spans = get_merged_exclusion_spans(sensors, y)
    beacons_inside_spans = get_beacons_inside_spans(
        beacons={s.beacon for s in sensors},
        spans=exclusion_spans,
        y=y)
    return sum(len(s) for s in exclusion_spans) - len(beacons_inside_spans)


def solve_part_2(sensors: list[Sensor], limit: int) -> int:
    for y in range(limit + 1):
        exclusions = get_merged_exclusion_spans(sensors, y)
        if len(exclusions) == 2:
            span = exclusions.pop()
            x = span.right + 1 if span.left <= 0 else span.left - 1
            return x * 4_000_000 + y


def calc_exclusion_spans(sensors: list[Sensor], y: int) -> set[Span]:
    exclusion_spans: set[Span] = set()
    for sensor in sensors:
        diff = sensor.pos.distance(sensor.beacon) - abs(sensor.pos.y - y)
        if diff < 0:
            continue
        exclusion_spans.add(Span(sensor.pos.x - diff, sensor.pos.x + diff))
    return exclusion_spans


def get_merged_exclusion_spans(sensors: list[Sensor], y: int) -> set[Span]:
    exclusion_spans = calc_exclusion_spans(sensors, y)
    return merge_all_overlaps(exclusion_spans)


def get_beacons_inside_spans(
        beacons: set[Coord], spans: set[Span], y: int) -> set[Coord]:
    beacons_on_same_row = {b for b in beacons if b.y == y}
    return {b for b in beacons_on_same_row
            if any(s.includes(b.x) for s in spans)}


def merge_first_overlap(spans: set[Span]) -> set[Span]:
    result = set(spans)
    for span1, span2 in combinations(spans, 2):
        if span1.touches(span2):
            result -= {span1, span2}
            result.add(span1.join(span2))
            break
    return result


def merge_all_overlaps(spans: set[Span]) -> set[Span]:
    while True:
        new_spans = merge_first_overlap(spans)
        if len(new_spans) == len(spans):
            return new_spans
        spans = new_spans


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
