from typing import Generator


def main(filename: str) -> tuple[int, int]:
    with open(filename, 'r') as fp:
        rucksacks = fp.read().splitlines()
    return solve_part_1(rucksacks), solve_part_2(rucksacks)


def solve_part_1(rucksacks: list[str]) -> int:
    compartments = [get_compartments(r) for r in rucksacks]
    return sum(get_prio(c1.intersection(c2).pop()) for c1, c2 in compartments)


def solve_part_2(rucksacks: list[str]) -> int:
    return sum(get_prio(set.intersection(*g).pop())
               for g in get_group(rucksacks))


def get_compartments(rucksack: str) -> tuple[set[str], set[str]]:
    return (
        set(rucksack[:len(rucksack)//2]),
        set(rucksack[len(rucksack)//2:]))


def get_group(rucksacks: list[str]) -> Generator:
    for i in range(0, len(rucksacks), 3):
        yield (set(r) for r in rucksacks[i:i + 3])


def get_prio(item: str) -> int:
    if item.islower():
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 27


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
