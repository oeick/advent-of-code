from itertools import cycle
from typing import Sequence
from functools import reduce
import operator

BLOCK_SIZE = 16


def get_sublist(target: list, start: int, length: int) -> list:
    cycler = cycle(target)
    return [next(cycler) for _ in range(start + length)][start:]


def replace_sublist(target_list: list, replace_list: list, start: int) -> list:
    target_pos = start
    for p_r in range(len(replace_list)):
        target_list[target_pos] = replace_list[p_r]
        target_pos = (target_pos + 1) % len(target_list)
    return target_list


def calc_sparse_hash(elements: Sequence, lengths: list[int], loops=1) -> list:
    result = list(elements)
    pos = 0
    for skip, length in enumerate(lengths * loops):
        sub = get_sublist(result, pos, length)
        rev = list(reversed(sub))
        result = replace_sublist(result, rev, pos)
        pos = (pos + length + skip) % len(result)
    return result


def calc_dense_hash(sparse_hash: list[int]) -> list[int]:
    xors = []
    for i_block in range(len(sparse_hash) // BLOCK_SIZE):
        block_start = i_block * BLOCK_SIZE
        block = sparse_hash[block_start:block_start + BLOCK_SIZE]
        xors.append(reduce(operator.xor, block))
    return xors


def convert_to_hex(dense_hash: list[int]) -> str:
    return ''.join(['%02x' % n for n in dense_hash])


def solve_part_1(numbers: Sequence[int], lengths: list[int]) -> int:
    sparse_hash = calc_sparse_hash(numbers, lengths)
    return sparse_hash[0] * sparse_hash[1]


def solve_part_2(numbers: Sequence[int], input_str: str) -> str:
    lengths = [ord(s) for s in input_str] + [17, 31, 73, 47, 23]
    sparse_hash = calc_sparse_hash(numbers, lengths, loops=64)
    dense_hash = calc_dense_hash(sparse_hash)
    return convert_to_hex(dense_hash)


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        input_string = fp.read()
    lengths = [int(s) for s in input_string.split(',')]
    return (solve_part_1(range(256), lengths),
            solve_part_2(range(256), input_string))


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
