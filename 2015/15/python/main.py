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


def calc_distributions(n_elements: int, n_containers: int) -> list[list[int]]:
    if n_containers == 1:
        return [[n_elements]]
    results = []
    for n in range(1, n_elements - n_containers + 2):
        sub_results = calc_distributions(n_elements - n, n_containers - 1)
        results += [[n] + sr for sr in sub_results]
    return results


def calc_score(
        teaspoons: list[int],
        ingredients: dict[str, dict],
        prop: str) -> int:
    return sum([teaspoons[n] * ingredients[i][prop]
                for n, i in enumerate(ingredients)])


def calc_calories(teaspoons: list[int], ingredients: dict[str, dict]) -> int:
    return sum([teaspoons[n] * ingredients[i]['calories']
                for n, i in enumerate(ingredients)])


def solve(ingredients: dict[str, dict]) -> (int, int):
    scores_part_1 = []
    scores_part_2 = []
    for teaspoons in calc_distributions(100, len(ingredients)):
        prop_scores = {p: calc_score(teaspoons, ingredients, p)
                       for p in PROPERTIES[:-1]}
        total_score = prod([max(0, ps) for ps in prop_scores.values()])
        if total_score > 0:
            scores_part_1.append(total_score)
        if calc_calories(teaspoons, ingredients) == 500:
            scores_part_2.append(total_score)
    return max(scores_part_1), max(scores_part_2)


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        lines = fp.readlines()
    ingredients = parse_ingredients(lines)
    return solve(ingredients)


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
