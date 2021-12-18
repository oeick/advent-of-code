CAVE_MAP = dict[str, set[str]]


def include_cave(cave_from: str, cave_to: str, cave_map: CAVE_MAP):
    if cave_from in cave_map:
        cave_map[cave_from].add(cave_to)
    else:
        cave_map[cave_from] = {cave_to}


def map_caves(connections: list[tuple[str, str]]) -> CAVE_MAP:
    cave_map: CAVE_MAP = {}
    for cave1, cave2 in connections:
        include_cave(cave1, cave2, cave_map)
        include_cave(cave2, cave1, cave_map)
    return cave_map


class Solver:
    caves: CAVE_MAP

    def __init__(self, caves: CAVE_MAP):
        self.caves = caves

    def filter_candidates(self,
                          trail: list[str],
                          cave: str,
                          second_visit_available: bool
                          ) -> set[tuple[str, bool]]:
        candidates = set()
        for candidate in [c for c in self.caves[cave] if c != 'start']:
            if candidate.isupper() or candidate not in trail:
                candidates.add((candidate, second_visit_available))
            else:
                if second_visit_available:
                    candidates.add((candidate, False))
        return candidates

    def count_paths(self,
                    trail: list[str],
                    cave: str,
                    second_visit_available: bool) -> int:
        if cave == 'end':
            return 1
        else:
            candidates = self.filter_candidates(
                trail, cave, second_visit_available)
            return sum(self.count_paths(trail + [cave], c, s)
                       for c, s in candidates)

    def solve_part_1(self) -> int:
        return self.count_paths([], 'start', second_visit_available=False)

    def solve_part_2(self) -> int:
        return self.count_paths([], 'start', second_visit_available=True)


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        lines = [t.split('-') for t in fp.read().splitlines()]
    caves = map_caves([(c[0], c[1]) for c in lines])
    return Solver(caves).solve_part_1(), Solver(caves).solve_part_2()


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
