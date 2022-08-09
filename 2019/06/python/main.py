from collections import defaultdict


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        lines = fp.read().splitlines()
    orbitmap = parse_orbitmap(lines)
    centermap = create_centermap(orbitmap)
    return solve(centermap)


def solve(centermap: dict[str, str]) -> (int, int):
    direct_orbits_you = get_direct_orbit_list('YOU', centermap)
    direct_orbits_santa = get_direct_orbit_list('SAN', centermap)
    first_mutual, count_you = search_first_mutual(
        direct_orbits_you, direct_orbits_santa)
    count_santa = count_orbits_from_santa_to_1st_mutual(
        direct_orbits_santa, first_mutual)
    return count_orbits(centermap), count_you + count_santa - 4


def count_orbits(centermap: dict[str, str]) -> int:
    orbit_count = 0
    for orbiter, center in centermap.items():
        orbit_count += 1
        while center in centermap:
            center = centermap[center]
            orbit_count += 1
    return orbit_count


def parse_orbitmap(lines: list[str]) -> dict[str, list[str]]:
    orbitmap_entries = [line.split(')') for line in lines]
    orbitmap = defaultdict(list)
    for center, orbiter in orbitmap_entries:
        orbitmap[center].append(orbiter)
    return orbitmap


def create_centermap(orbitmap: dict[str, list[str]]) -> dict[str, str]:
    centermap = {}
    for center, orbiter_list in orbitmap.items():
        for orbiter in orbiter_list:
            centermap[orbiter] = center
    return centermap


def get_direct_orbit_list(start: str, centermap: dict[str, str]) -> list[str]:
    direct_orbit_list = []
    center = start
    while center in centermap:
        direct_orbit_list.append(center)
        center = centermap[center]
    return direct_orbit_list


def search_first_mutual(direct_orbits_you: list[str],
                        direct_orbits_santa: list[str]) -> (str, int):
    count_you = 0
    for orbiter in direct_orbits_you:
        count_you += 1
        if orbiter in direct_orbits_santa:
            first_mutual = orbiter
            return first_mutual, count_you


def count_orbits_from_santa_to_1st_mutual(
        direct_orbits_santa: list[str], first_mutual: str) -> int:
    count_santa = 0
    for orbiter in direct_orbits_santa:
        count_santa += 1
        if orbiter == first_mutual:
            return count_santa


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
