from typing import NamedTuple, Self, Optional


class Node(NamedTuple):
    childs: list[Self]
    data: list[Optional[int]]
    parent: Optional[Self]

    @staticmethod
    def of(n_childs: int, n_data: int) -> Self:
        """ Creates new empty node with no parent."""
        return Node([None] * n_childs, [None] * n_data, None)

    def make(self, n_childs: int, n_data: int) -> Self:
        """ Creates new node which is a child of this node."""
        return Node([None] * n_childs, [None] * n_data, self)

    def fillin_data(self, nums: list[int], i: int) -> (Self, int):
        n_data = len(self.data)
        for i_data, num in enumerate(nums[i:i + n_data]):
            self.data[i_data] = num
        return self.parent, i + n_data

    def create_child(self, nums: list[int], i: int) -> (Self, int):
        new_node = self.make(*nums[i:i + 2])
        self.childs[len(list(filter(None, self.childs)))] = new_node
        return new_node, i + 2

    def complete(self, nums: list[int], i: int) -> (Self, int):
        return self.fillin_data(nums, i) if all(self.childs) \
            else self.create_child(nums, i)


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
