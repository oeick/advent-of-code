def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        image = fp.read().strip()
    size = (25, 6)
    layers = get_layers(image, size)
    return solve_part_1(layers), solve_part_2(layers, size)


def solve_part_1(layers: list[str]) -> int:
    count_0 = [layer.count('0') for layer in layers]
    i_fewest = count_0.index(min(count_0))
    count_1 = layers[i_fewest].count('1')
    count_2 = layers[i_fewest].count('2')
    return count_1 * count_2


def solve_part_2(layers: list[str], size: tuple[int, int]) -> str:
    layers_lines = get_lines_of_layers(layers, size)
    result_lines = stack_lines(layers_lines, size)
    return '\n'.join(line.replace('0', ' ') for line in result_lines)


def get_layers(image: str, size: tuple[int, int]) -> list[str]:
    width, height = size
    length = width * height
    n_layer = len(image) // length
    return [image[i * length:(i + 1) * length] for i in range(n_layer)]


def get_lines_of_layers(
        layers: list[str], size: tuple[int, int]) -> list[list[str]]:
    w, h = size
    return [[c[i * w:(i + 1) * w] for i in range(h)] for c in layers]


def stack_lines(
        layer_lines: list[list[str]], size: tuple[int, int]) -> list[str]:
    width, height = size
    result_lines = ['2' * width] * height
    for layer in layer_lines:
        for i_line in range(height):
            layer_line = layer[i_line]
            result_line = result_lines[i_line]
            line = ''.join([layer_line[i]
                            if result_line[i] == '2'
                            else result_line[i]
                            for i in range(width)])
            result_lines[i_line] = line
    return result_lines


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
