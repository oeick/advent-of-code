def solve(banks: list[int]) -> (int, int):
    configs = [banks]
    new_banks = redistribute_blocks(banks)
    while new_banks not in configs:
        configs.append(new_banks)
        new_banks = redistribute_blocks(new_banks)
    loop_start = configs.index(new_banks)
    return len(configs), len(configs) - loop_start


def redistribute_blocks(banks: list[int]) -> list[int]:
    blocks_to_redistribute = max(banks)
    target_bank = banks.index(blocks_to_redistribute)
    result = list(banks)
    result[target_bank] = 0
    for i in range(blocks_to_redistribute):
        target_bank = (target_bank + 1) % len(result)
        result[target_bank] += 1
    return result


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        banks = [int(n) for n in fp.read().split()]
    return solve(banks)


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
