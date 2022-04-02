from collections import Counter
from typing import Callable, Iterable


def has_no_duplicates(phrase: str) -> bool:
    return all(v == 1 for v in Counter(phrase.split()).values())


def has_no_anagrams(phrase: str) -> bool:
    sorted_chars = [tuple(sorted(w)) for w in phrase.split()]
    return all(v == 1 for v in Counter(sorted_chars).values())


def solve(passphrases: Iterable[str], policy: Callable) -> int:
    return sum(policy(p) for p in passphrases)


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        passphrases = fp.read().splitlines()
    return (solve(passphrases, has_no_duplicates),
            solve(passphrases, has_no_anagrams))


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
