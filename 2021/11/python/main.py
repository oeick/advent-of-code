from itertools import count

LEVELS = list[list[int]]


class Solver:
    size: int
    levels: LEVELS

    def __init__(self, levels):
        self.size = len(levels)
        self.levels = list([list(row) for row in levels])

    def coordinates(self) -> (int, int):
        for y in range(self.size):
            for x in range(self.size):
                yield x, y

    def neighbors(self, x: int, y: int) -> (int, int):
        for xn, yn in [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
                       (x - 1, y), (x + 1, y),
                       (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]:
            if 0 <= xn < self.size and 0 <= yn < self.size:
                yield xn, yn

    def energize_neighbors(self, x: int, y: int):
        self.levels[x][y] = 0
        for x2, y2 in self.neighbors(x, y):
            if self.levels[x2][y2] > 0:
                self.levels[x2][y2] += 1

    def do_all_flashes(self) -> int:
        flash_counter = 0
        for x, y in self.coordinates():
            if self.levels[x][y] > 9:
                flash_counter += 1
                self.energize_neighbors(x, y)
        return flash_counter

    def increase_energy_levels(self):
        for x, y in self.coordinates():
            self.levels[x][y] += 1

    def count_flashes(self) -> int:
        self.increase_energy_levels()
        total_flashes = 0
        while local_flashes := self.do_all_flashes():
            total_flashes += local_flashes
        return total_flashes

    def solve_part_1(self, steps: int) -> int:
        total = 0
        for i in range(steps):
            total += self.count_flashes()
        return total

    def solve_part_2(self) -> int:
        for i in count():
            self.count_flashes()
            if sum(sum(row) for row in self.levels) == 0:
                return i + 1


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        levels = [[int(n) for n in row] for row in fp.read().splitlines()]
    return Solver(levels).solve_part_1(100), Solver(levels).solve_part_2()


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
