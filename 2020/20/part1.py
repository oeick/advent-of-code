import functools

with open('input.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file]


tiles = {}
for i, line in enumerate(lines):
    if line.startswith('Tile'):
        _, number = line.split(' ')
        number = number[:-1]
        tile = lines[i+1:i+11]
        tiles[number] = tile


def get_edges(tile):
    edges = [tile[0], tile[-1],
             tile[0][::-1], tile[-1][::-1]]
    left = ''.join([row[0] for row in tile])
    right = ''.join([row[-1] for row in tile])
    edges += [left, right, left[::-1], right[::-1]]
    return edges


def is_corner(number, tiles):
    edges0 = get_edges(tiles[number])
    connected = set()
    for n1, tile1 in tiles.items():
        if n1 != number:
            edges1 = get_edges(tile1)
            for e1 in edges1:
                if e1 in edges0:
                    connected.add(n1)
    if len(connected) == 2:
        return True
    return False


corner = []
for t in tiles:
    if is_corner(t, tiles):
        corner.append(t)
        if len(corner) == 4:
            break

print(functools.reduce(lambda a, b: int(a)*int(b), corner))
