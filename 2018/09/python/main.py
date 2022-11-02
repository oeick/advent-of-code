import re

from node import Node

PATTERN = re.compile(r'(\d+) players; last marble is worth (\d+) points')


def main(filename: str) -> tuple[int, int]:
    with open(filename, 'r') as fp:
        line = fp.read()
    n_players, last_marble = parse_line(line)
    return solve(n_players, last_marble)


def parse_line(line: str) -> tuple[int, int]:
    match = PATTERN.match(line)
    return int(match.group(1)), int(match.group(2))


def solve(n_players: int, last_marble: int) -> tuple[int, int]:
    return (calculate_highscore(n_players, last_marble),
            calculate_highscore(n_players, last_marble * 100))


def calculate_highscore(n_players: int, last_marble: int) -> int:
    player = 0
    score = [0] * n_players
    circle = Node(0)
    circle.left = circle.right = circle
    for marbel_to_place in range(1, last_marble + 1):
        player = player + 1 if player < n_players else 1
        if marbel_to_place % 23 == 0:
            score[player - 1] += marbel_to_place
            circle = circle.go_left(7)
            score[player - 1] += circle.value
            circle = circle.remove()
        else:
            circle = circle.go_right(1)
            circle = circle.insert(marbel_to_place)
    return max(score)


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
