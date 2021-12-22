IMAGE = set[tuple[int, int]]


def get_boundary(image: IMAGE) -> (int, int, int, int):
    x1 = min(image)[0]
    x2 = max(image)[0]
    y1 = min(image, key=lambda p: p[1])[1]
    y2 = max(image, key=lambda p: p[1])[1]
    return x1, y1, x2, y2


def pad_image(image: IMAGE) -> IMAGE:
    image = set(image)
    x1, y1, x2, y2 = get_boundary(image)
    for x in range(x1 - 1, x2 + 2):
        image.add((x, y1 - 1))
        image.add((x, y2 + 1))
    for y in range(y1, y2 + 1):
        image.add((x1 - 1, y))
        image.add((x2 + 1, y))
    return image


def get_index(x: int, y: int, image: IMAGE) -> int:
    index = 0
    for b, xw, yw in ((256, x - 1, y - 1), (128, x, y - 1), (64, x + 1, y - 1),
                      (32, x - 1, y), (16, x, y), (8, x + 1, y),
                      (4, x - 1, y + 1), (2, x, y + 1), (1, x + 1, y + 1)):
        if (xw, yw) in image:
            index |= b
    return index


def enhance(algorithm: str, image: IMAGE, is_infinity_empty: bool) -> IMAGE:
    x1, y1, x2, y2 = get_boundary(image)
    if not is_infinity_empty:
        image = pad_image(image)
        image = pad_image(image)
    return {(x, y)
            for y in range(y1 - 1, y2 + 2)
            for x in range(x1 - 1, x2 + 2)
            if algorithm[get_index(x, y, image)] == '#'}


def solve(algorithm: str, image: IMAGE, steps=2) -> int:
    for _ in range(steps // 2):
        image = enhance(algorithm, image, True)
        image = enhance(algorithm, image, algorithm[0] == '.')
    return len(image)


def parse_image(lines: list[str]) -> IMAGE:
    return {(x, y)
            for y, line in enumerate(lines)
            for x in range(len(line))
            if lines[y][x] == '#'}


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        lines = fp.read().splitlines()
    algorithm, image = lines[0], parse_image(lines[2:])
    return solve(algorithm, image), solve(algorithm, image, 50)


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
