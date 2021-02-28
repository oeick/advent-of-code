COMBIS = list[list[int]]


def get_combinations(total: int, values: list[int]) -> COMBIS:
    results = []
    for i, value in enumerate(values):
        if value < total:
            if i < len(values) - 1:
                sub_results = get_combinations(total - value, values[i + 1:])
                if sub_results:
                    results += [[value] + r for r in sub_results]
        elif value == total:
            results.append([value])
        else:
            break
    return results


def get_all_combinations(total: int, containers: list[int]) -> COMBIS:
    return get_combinations(total, sorted(containers))


def get_shortest_combinations(all_combinations: COMBIS) -> COMBIS:
    minimum = len(min(all_combinations, key=len))
    return [c for c in all_combinations if len(c) == minimum]


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        containers = [int(line) for line in fp.readlines()]
    all_combinations = get_all_combinations(150, containers)
    smallest_combinations = get_shortest_combinations(all_combinations)
    return len(all_combinations), len(smallest_combinations)


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
