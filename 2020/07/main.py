import re
from functools import lru_cache

with open('input.txt', 'r') as fp:
    lines = [line.strip() for line in fp.readlines()]

pattern = re.compile(r'(.*) bags contain (.*)\.')
sub_pattern = re.compile(r'(\d+) (\w+ \w+)')

bags = {}
for line in lines:
    matches = pattern.match(line)
    bag_color, contents = matches[1], matches[2]
    sub_matches = sub_pattern.findall(contents)
    bags[bag_color] = [(int(m[0]), m[1]) for m in sub_matches]


def contains_shiny_gold(color):
    for _, sub_color in bags[color]:
        if sub_color == 'shiny gold':
            return True
        elif contains_shiny_gold(sub_color):
            return True
    return False


count = sum(1 for c in bags.keys() if contains_shiny_gold(c))

print(count)


@lru_cache
def count_content(color):
    return sum(n + n * count_content(c) for n, c in bags[color])


print(count_content('shiny gold'))
