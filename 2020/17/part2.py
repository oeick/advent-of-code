input_string = """
##.#####
#.##..#.
.##...##
###.#...
.#######
##....##
###.###.
.#.#.#.."""


def calc_neighbor_coords(x0, y0, z0, w0):
    return ((x, y, z, w)
            for x in (x0-1, x0, x0+1)
            for y in (y0-1, y0, y0+1)
            for z in (z0-1, z0, z0+1)
            for w in (w0-1, w0, w0+1)
            if x != x0 or y != y0 or z != z0 or w != w0)


def count_active_neighbors(x0, y0, z0, w0, state):
    coords = calc_neighbor_coords(x0, y0, z0, w0)
    return sum(1 for c in coords if c in state)


def generate_next_state(prev_state):
    next_state = {cube
                  for cube in prev_state
                  if 2 <= count_active_neighbors(*cube, state=prev_state) <= 3}
    inactive = {c
                for a in prev_state
                for c in calc_neighbor_coords(*a)
                if c not in prev_state}
    for cube in inactive:
        if count_active_neighbors(*cube, state=prev_state) == 3:
            next_state.add(cube)
    return next_state


current_state = {(x, y, 0, 0)
                 for y, r in enumerate(input_string.split())
                 for x, s in enumerate(r)
                 if s == '#'}

for cycle in range(6):
    current_state = generate_next_state(current_state)

print(len(current_state))
