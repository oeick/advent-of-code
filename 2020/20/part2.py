ImageData = list[list[bool]]

with open('input.txt', 'r') as input_file:
    lines: list[str] = [line.strip() for line in input_file]

prepared_tile_rows: dict[int, list] = {}
for i_line, line in enumerate(lines):
    if line.startswith('Tile'):
        _, number_str = line.split(' ')
        prepared_tile_rows[int(number_str[:-1])] = lines[i_line + 1:i_line + 11]


class Tile:
    number: int
    data: ImageData

    def __init__(self, number: int, data: ImageData):
        self.number = number
        self.data = data

    @classmethod
    def of(cls, number: int, rows: list[str]):
        return Tile(number, [[c == '#' for c in row] for row in rows])

    def __str__(self) -> str:
        return str(self.number)

    def __repr__(self) -> str:
        return str(self.number)


def cloned(tile: Tile) -> Tile:
    return Tile(tile.number, [list(row) for row in tile.data])


def empty(tile: Tile) -> Tile:
    return Tile(tile.number, [[False] * len(row) for row in tile.data])


def flip_image(image: list[list[bool]]) -> list[list[bool]]:
    return list(image[::-1])


def flipped(tile: Tile) -> Tile:
    return Tile(tile.number, tile.data[::-1])


def rotate1_image(image: ImageData) -> ImageData:
    new = [[False for _ in range(len(image[0]))] for _ in range(len(image))]
    for i, source_row in enumerate(image[::-1]):
        for j, element in enumerate(source_row):
            new[j][i] = element
    return new


def rotated1(tile: Tile) -> Tile:
    new = empty(tile)
    for i, source_row in enumerate(tile.data[::-1]):
        for j, element in enumerate(source_row):
            new.data[j][i] = element
    return new


def rotate2_image(image: ImageData) -> ImageData:
    return [row[::-1] for row in image[::-1]]


def rotated2(tile: Tile) -> Tile:
    return Tile(tile.number, [row[::-1] for row in cloned(tile).data[::-1]])


def rotate3_image(image: ImageData) -> ImageData:
    return rotate2_image(rotate1_image(image))


def rotated3(tile: Tile) -> Tile:
    return rotated2(rotated1(tile))


def get_modi_image(image: ImageData) -> list[ImageData]:
    return [
        image,
        rotate1_image(image),
        rotate2_image(image),
        rotate3_image(image),
        flip_image(image),
        flip_image(rotate1_image(image)),
        flip_image(rotate2_image(image)),
        flip_image(rotate3_image(image))]


def get_modi(tile: Tile) -> list[Tile]:
    return [
        cloned(tile),
        rotated1(tile),
        rotated2(tile),
        rotated3(tile),
        flipped(tile),
        flipped(rotated1(tile)),
        flipped(rotated2(tile)),
        flipped(rotated3(tile))]


def get_interface(main_tile: Tile, target_tile: Tile) -> dict[str, Tile]:
    target_modi: list[Tile] = get_modi(target_tile)
    directions = {
        'north': [t for t in target_modi if t.data[-1] == main_tile.data[0]],
        'south': [t for t in target_modi if t.data[0] == main_tile.data[-1]],
        'east': [t for t in target_modi if [r[0] for r in t.data] == [r[-1] for r in main_tile.data]],
        'west': [t for t in target_modi if [r[-1] for r in t.data] == [r[0] for r in main_tile.data]]}
    return {k: v[0] for k, v in directions.items() if len(v) > 0}


def convert_to_tiles(all_tile_rows):
    tiles: dict[int, Tile] = {}
    for number, tile_rows in all_tile_rows.items():
        tiles[number] = Tile.of(number, tile_rows)
    return tiles


def get_neighbours(tile: Tile, tiles: dict[int, Tile]) -> dict[str, Tile]:
    neighbours = {}
    for other_number in [tn for tn in tiles if tn != tile.number]:
        neighbours.update(get_interface(tile, tiles[other_number]))
    return neighbours


def align_tiles(tiles: dict[int, Tile]) -> list[list[Tile]]:
    current_tile = None
    for number, tile in tiles.items():
        neighbours = get_neighbours(tile, tiles)
        if 'west' not in neighbours and 'north' not in neighbours:
            current_tile = tile

    rows = []
    row = [current_tile]
    while True:
        current_neighbours = get_neighbours(current_tile, tiles)
        if 'east' in current_neighbours:
            current_tile = current_neighbours['east']
            row.append(current_tile)
        else:
            rows.append(row)
            first_neighbours = get_neighbours(row[0], tiles)
            if 'south' in first_neighbours:
                current_tile = first_neighbours['south']
                row = [current_tile]
            else:
                break
    return rows


def build_image(aligned_table: list[list[Tile]]) -> list[list[bool]]:
    rows_per_tile = len(aligned_table[0][0].data)
    image_rows = []
    for alignment_row in aligned_table:
        for i_row in range(1, rows_per_tile - 1):
            image_row = []
            for tile in alignment_row:
                image_row += tile.data[i_row][1:-1]
            image_rows.append(image_row)
    return image_rows


def find_monsters(image):
    monster = [
        [False, False, False, False, False, False,
         False, False, False, False, False, False,
         False, False, False, False, False, False,
         True, False],
        [True, False, False, False, False, True,
         True, False, False, False, False, True,
         True, False, False, False, False, True,
         True, True],
        [False, True, False, False, True, False,
         False, True, False, False, True, False,
         False, True, False, False, True, False,
         False, False]]
    counter = 0
    for mode in get_modi_image(image):
        for row_offset in range(len(image) - len(monster)):
            for column_offset in range(len(image[0]) - len(monster[0])):
                is_monster = True
                for row in range(len(monster)):
                    for column in range(len(monster[0])):
                        m = monster[row][column]
                        i = mode[row + row_offset][column + column_offset]
                        if m and not i:
                            is_monster = False
                            break
                    if not is_monster:
                        break
                if is_monster:
                    counter += 1
    return counter


tiles_objects: dict[int, Tile] = convert_to_tiles(prepared_tile_rows)
aligned_tiles: list[list[Tile]] = align_tiles(tiles_objects)
assembled_image = build_image(aligned_tiles)

monster_count = find_monsters(assembled_image)
wave_count = sum(sum(1 if b else 0 for b in row) for row in assembled_image)
print(wave_count - 15 * monster_count)
