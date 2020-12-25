import re
from functools import reduce

with open('input.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file]

line_pattern = re.compile(r'^(.*) \(contains (.*)\)$')

ing_per_food = []
alg_per_food = []
all_alg = set()

for line in lines:
    match = line_pattern.match(line)
    ing_per_food.append(set(match[1].split()))
    alg_per_food.append(set(match[2].split(', ')))
    for a in alg_per_food[-1]:
        all_alg.add(a)

ing_candidates_per_alg = {}
for allergen in all_alg:
    ing_candidates_per_alg[allergen] = reduce(
        lambda ing1, ing2: ing1.intersection(ing2),
        [ing for ing, alg in zip(ing_per_food, alg_per_food)
         if allergen in alg])

assigned = {}

while len(assigned) < len(all_alg):
    unambiguously = min(
        ing_candidates_per_alg,
        key=lambda a: len(ing_candidates_per_alg[a]))
    assigned[unambiguously] = ing_candidates_per_alg[unambiguously].pop()
    del(ing_candidates_per_alg[unambiguously])
    for ingredient_set in ing_candidates_per_alg.values():
        if assigned[unambiguously] in ingredient_set:
            ingredient_set.remove(assigned[unambiguously])

all_ing = {ing for ing_list in ing_per_food for ing in ing_list}

ing_free_of_alg = {ing for ing in all_ing if ing not in assigned.values()}

print(sum(1 for ings in ing_per_food for ing in ings if ing in ing_free_of_alg))

print(','.join(assigned[alg] for alg in sorted(assigned)))
