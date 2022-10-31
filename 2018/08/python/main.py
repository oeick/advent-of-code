from node import Node


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        numbers = [int(n) for n in fp.read().split(' ')]
    root_node = create_nodes(numbers)
    return solve_part_1(root_node), solve_part_2(root_node)


def solve_part_1(root_node: Node) -> int:
    return sum_data(root_node)


def solve_part_2(root_node: Node) -> int:
    return calculate_value(root_node)


def create_nodes(nums: list[int]) -> Node:
    i = 2
    n_childs, n_data = nums[0:i]
    root = current_node = Node.of(n_childs, n_data)
    while current_node:
        current_node, i = current_node.complete(nums, i)
    return root


def sum_data(node: Node) -> int:
    return sum(node.data) + sum(sum_data(c) for c in node.childs)


def calculate_value(node: Node) -> int:
    if node.childs:
        return sum(calculate_value(node.childs[i - 1])
                   for i in node.data if i and i <= len(node.childs))
    else:
        return sum(node.data)


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
