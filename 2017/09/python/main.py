import re


def remove_canceled_chars(stream: str) -> str:
    return re.sub('!.', '', stream)


def remove_garbage(stream: str) -> str:
    stream_without_canceled_chars = remove_canceled_chars(stream)
    return re.sub('<.*?>', '', stream_without_canceled_chars)


def solve_part_1(stream: str) -> int:
    cleaned_stream = remove_garbage(stream)
    level, score = 0, 0
    for char in cleaned_stream:
        if char == '{':
            level += 1
            score += level
        elif char == '}':
            level -= 1
    return score


def solve_part_2(stream: str) -> int:
    stream_without_canceled_chars = remove_canceled_chars(stream)
    matches = re.findall('<(.*?)>', stream_without_canceled_chars)
    return sum(len(m) for m in matches)


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        stream = fp.read()
    return solve_part_1(stream), solve_part_2(stream)


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
