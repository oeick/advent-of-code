import re
from math import prod

PATTERN = re.compile(r'-?\d+|^\w+')
PROPERTIES = ['capacity', 'durability', 'flavor', 'texture', 'calories']


def parse_ingredients(lines: list[str]) -> dict[str, dict]:
    ingredients = {}
    for line in lines:
        ingredient, *properties = PATTERN.findall(line)
        ingredients[ingredient] = dict(zip(
            PROPERTIES,
            [int(p) for p in properties]))
    return ingredients


def calc_teaspoons(ingredients: list[str]) -> list[dict[str, int]]:
    teaspoons = []
    n = [1 for _ in ingredients[:-1]]
    while n[0] < 100 - len(n):
        teaspoons.append(dict(zip(ingredients, n + [100 - sum(n)])))
        i = len(n) - 1
        while True:
            if sum(n) < 99:
                n[i] += 1
                break
            elif i > 0:
                n[i] = 1
                n[i - 1] += 1
            i -= 1
    return teaspoons


def calc_score(
        teaspoons: dict[str, int],
        ingredients: dict[str, dict],
        prop: str) -> int:
    return sum([teaspoons[i] * ingredients[i][prop]
                for i in ingredients])


def solve(ingredients: dict[str, dict]) -> (int, int):
    scores = []
    for teaspoons in calc_teaspoons(list(ingredients.keys())):
        prop_scores = {p: calc_score(teaspoons, ingredients, p)
                       for p in PROPERTIES[:-1]}
        total_score = prod([max(0, ps) for ps in prop_scores.values()])
        if total_score > 0:
            scores.append(total_score)
    return max(scores), 0


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        lines = fp.readlines()
    ingredients = parse_ingredients(lines)
    return solve(ingredients)


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
