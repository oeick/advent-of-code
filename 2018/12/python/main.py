def main(filename: str) -> tuple[int, int]:
    with open(filename, 'r') as fp:
        lines = fp.read().splitlines()
    return solve(lines)


def solve(lines: list[str]) -> tuple[int, int]:
    start_index = 0
    initial_state = lines[0][15:]
    rules = parse_growing_rules_from_notes(lines[2:])
    return (solve_part_1(start_index, initial_state, rules),
            solve_part_2(start_index, initial_state, rules))


def solve_part_1(start_index: int,
                 initial_state: str,
                 rules: list[str]) -> int:
    index_20, state_20 = get_state_of_generation_n(
        20, start_index, initial_state, rules)
    return calculate_sum_of_pot_numbers(index_20, state_20)


def solve_part_2(start_index: int,
                 initial_state: str,
                 rules: list[str]) -> int:
    generation_stable, index_stable, state_stable = get_stable_state(
        start_index, initial_state, rules)
    fifty_billion_index = 50_000_000_000 - generation_stable + index_stable
    return calculate_sum_of_pot_numbers(fifty_billion_index, state_stable)


def parse_growing_rules_from_notes(lines: list[str]) -> list[str]:
    rules_for_growing = [line[:5] for line in lines if line[-1] == '#']
    return rules_for_growing


def get_state_of_generation_n(
        n: int,
        start_index: int,
        initial_state: str,
        rules: list[str]) -> tuple[int, str]:
    index = start_index
    state = initial_state
    for _ in range(n):
        index, state = apply_rules(index, state, rules)
    return index, state


def get_stable_state(
        start_index: int,
        initial_state: str,
        rules: list[str]) -> tuple[int, int, str]:
    index = start_index
    state = initial_state
    prev_state = ''
    generation = 0
    while state != prev_state:
        prev_state = state
        index, state = apply_rules(index, state, rules)
        generation += 1
    return generation, index, state


def calculate_sum_of_pot_numbers(index: int, state: str) -> int:
    return sum([i + index for i, p in enumerate(state) if p == '#'])


def apply_rules(
        start_index: int, state: str, rules: list[str]) -> tuple[int, str]:
    current_state = apply_patterns(init_state="...." + state + "....",
                                   rules=rules)
    first_plant_index = current_state.index('#')
    last_plant_index = current_state[-1::-1].index('#')
    next_state_str = ''.join(current_state[first_plant_index:-last_plant_index])
    new_start_index = start_index - 4 + first_plant_index
    return new_start_index, next_state_str


def apply_patterns(init_state: str, rules: list[str]) -> list[str]:
    next_state = ["."] * len(init_state)
    for pattern in rules:
        index = 0
        relative_index = 0
        while relative_index > -1 and index < len(init_state):
            relative_index = init_state[index:].find(pattern)
            if relative_index > -1:
                index = index + relative_index
                next_state[index + 2] = '#'
                index += 1
    return next_state


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
