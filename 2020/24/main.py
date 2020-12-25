import re

with open('input.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file]

instruction_pattern = re.compile(r'(w|nw|ne|e|se|sw)')

all_instruction_lists = [instruction_pattern.findall(line) for line in lines]

translation = {'w': -1,
               'nw': -1j,
               'ne': 1-1j,
               'e': 1,
               'se': 1j,
               'sw': -1+1j}

all_steps = [[translation[instruction] for instruction in instruction_list]
             for instruction_list in all_instruction_lists]


switched = [sum(steps) for steps in all_steps]
black = {b for b in switched if switched.count(b) == 1}

print(len(black))


def get_neighours(tile):
    return {tile + d for d in translation.values()}


for _ in range(100):
    candidates = set(black)
    for tile in black:
        candidates = candidates.union(get_neighours(tile))

    next_blacks = set()
    for tile in candidates:
        black_neighbours = sum(1 for n in get_neighours(tile) if n in black)
        if tile in black:
            if 1 <= black_neighbours <= 2:
                next_blacks.add(tile)
        else:
            if black_neighbours == 2:
                next_blacks.add(tile)

    black = next_blacks

print(len(black))
