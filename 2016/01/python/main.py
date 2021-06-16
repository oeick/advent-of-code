rotations = {
    'N': {'R': 'E', 'L': 'W'},
    'E': {'R': 'S', 'L': 'N'},
    'S': {'R': 'W', 'L': 'E'},
    'W': {'R': 'N', 'L': 'S'},
}


def solve(instructions: list[str]) -> (int, int):
    x, y = 0, 0
    face = 'N'
    path = [(x, y)]
    for instruction in instructions:
        turn = instruction[0]
        blocks = int(instruction[1:])
        face = rotations[face][turn]
        if face == 'N':
            path += [(x, y + d) for d in range(1, blocks + 1)]
        elif face == 'E':
            path += [(x + d, y) for d in range(1, blocks + 1)]
        elif face == 'S':
            path += [(x, y - d) for d in range(1, blocks + 1)]
        else:
            path += [(x - d, y) for d in range(1, blocks + 1)]
        x, y = path[-1]
    for coords in path:
        if path.count(coords) > 1:
            break
    else:
        coords = 0, 0
    return abs(x + y), sum(abs(v) for v in coords)


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        lines = fp.read()
    return solve(lines.split(', '))


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
