from itertools import product

GRID_SIZE: int = 300


def main(filename: str) -> tuple[str, str]:
    with open(filename, 'r') as fp:
        grid_serial_number = int(fp.read())
    power_array_input = calculate_power_level_array(grid_serial_number)
    return (
        solve_part_1(power_array_input),
        solve_part_2(power_array_input))


def solve_part_1(power_array_input: list[list[int]]) -> str:
    return '{},{}'.format(*find_max_power_square(power_array_input))


def solve_part_2(power_array_input: list[list[int]]) -> str:
    return '{},{},{}'.format(*find_max_power_square_nxn(power_array_input))


def calculate_power_level(x: int, y: int, serial_number: int) -> int:
    rack_id = x + 10
    power_level_0 = (rack_id * y + serial_number) * rack_id
    power_level = int(str(power_level_0)[-3]) - 5
    return power_level


def calculate_power_level_array(serial_number: int) -> list[list[int]]:
    return [[calculate_power_level(x, y, serial_number)
             for y in range(1, GRID_SIZE + 1)]
            for x in range(1, GRID_SIZE + 1)]


def calculate_total_power_level(
        x: int, y: int,
        power_array: list[list[int]],
        square_size: int = 3) -> int:
    powers = [
        power_array[x + dx][y + dy] for dx, dy in product(
            range(-1, square_size - 1),
            range(-1, square_size - 1))]
    return sum(powers)


def find_max_power_square(
        power_array: list[list[int]],
        square_size: int = 3) -> tuple[int, int, int]:
    """Returned tuple: x, y, power level"""
    square_power_levels = [
        (x, y, calculate_total_power_level(x, y, power_array, square_size))
        for x, y in product(
            range(1, GRID_SIZE + 2 - square_size),
            range(1, GRID_SIZE + 2 - square_size))]
    max_square = max(square_power_levels, key=lambda s: s[2])
    return max_square


def find_max_power_square_nxn(
        power_array: list[list[int]]) -> tuple[int, int, int, int]:
    """Returned tuple: x, y, square size, power level"""
    nxn_power_max = 0
    x_max, y_max = None, None
    for size in range(1, GRID_SIZE + 1):
        x, y, nxn_power = find_max_power_square(power_array, size)
        if nxn_power > nxn_power_max:
            nxn_power_max = nxn_power
            x_max, y_max = x, y
        elif nxn_power < nxn_power_max:
            return x_max, y_max, size - 1, nxn_power_max


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
