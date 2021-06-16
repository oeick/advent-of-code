ROTATIONS = {
    'N': {'R': 'E', 'L': 'W'},
    'E': {'R': 'S', 'L': 'N'},
    'S': {'R': 'W', 'L': 'E'},
    'W': {'R': 'N', 'L': 'S'},
}


def build_path(instructions: list[str]) -> list[tuple]:
    x, y = 0, 0
    face = 'N'
    path = [(x, y)]
    for instruction in instructions:
        turn = instruction[0]
        blocks = int(instruction[1:])
        face = ROTATIONS[face][turn]
        if face == 'N':
            path += [(x, y + d) for d in range(1, blocks + 1)]
        elif face == 'E':
            path += [(x + d, y) for d in range(1, blocks + 1)]
        elif face == 'S':
            path += [(x, y - d) for d in range(1, blocks + 1)]
        else:
            path += [(x - d, y) for d in range(1, blocks + 1)]
        x, y = path[-1]
    return path


def find_first_location_visited_twice(path: list[tuple]) -> tuple:
    for coords in path:
        if path.count(coords) > 1:
            return coords


def solve(instructions: list[str]) -> (int, int):
    path = build_path(instructions)
    twice = find_first_location_visited_twice(path)
    calc_dist = lambda vec: sum(abs(x) for x in vec) if vec else -1
    return calc_dist(path[-1]), calc_dist(twice)


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        lines = fp.read()
    return solve(lines.split(', '))


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
