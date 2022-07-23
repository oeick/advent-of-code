def solve_part_1(polymer: str) -> int:
    return len(remove_opposites(polymer))


def solve_part_2(polymer: str) -> int:
    return len(find_shortest_polymer_with_removed_unit_type(polymer))


def remove_opposites(polymer: str) -> str:
    i, i_max = 0, len(polymer) - 1
    while i < i_max:
        if i < i_max and is_reaction_possible(*polymer[i:i+2]):
            polymer = polymer[0:i] + polymer[i + 2:i_max + 1]
            i_max = len(polymer) - 1
            i = max(0, i - 1)
        else:
            i += 1
    return polymer


def find_shortest_polymer_with_removed_unit_type(polymer: str) -> str:
    shortest = polymer
    for unit_type in set(polymer):
        shortened = remove_opposites(remove_type(polymer, unit_type))
        shortest = min(shortened, shortest, key=len)
    return shortest


def remove_type(polymer: str, unit_type: str) -> str:
    return polymer.replace(unit_type.lower(), '').replace(unit_type.upper(), '')


def is_reaction_possible(left: str, right: str) -> bool:
    return left.lower() == right.lower() and left.islower() != right.islower()


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        polymer = fp.read()
    return solve_part_1(polymer), solve_part_2(polymer)


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
