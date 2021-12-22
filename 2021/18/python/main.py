from __future__ import annotations

from dataclasses import dataclass
from math import ceil
from typing import Optional, Iterator


@dataclass
class Node:
    prev: Optional[Node]
    next: Optional[Node]
    value: int

    def __repr__(self) -> str:
        current = self
        string = value_to_string(current.value)
        while current.next:
            string += value_to_string(current.next.value)
            current = current.next
        return string


def clone_nodes(node: Node) -> Node:
    current = node
    clone = Node(None, None, current.value)
    first_clone = clone
    while current.next:
        clone.next = Node(clone, None, current.next.value)
        current, clone = current.next, clone.next
    return first_clone


def value_to_string(value: int) -> str:
    if value < 0:
        return {-1: '[', -3: ']'}[value]
    elif value < 10:
        return str(value)
    else:
        return chr(ord('A') + value - 10)


def find_regular(node: Node, forward=True) -> Optional[Node]:
    current = node.next if forward else node.prev
    while current:
        if current.value >= 0:
            return current
        current = current.next if forward else current.prev


def find_last(node: Node) -> Node:
    current = node
    while current.next:
        current = current.next
    return current


def explode(bomb: Node):
    last_regular = find_regular(bomb, forward=False)
    next_regular = find_regular(bomb.next)
    if last_regular:
        last_regular.value += bomb.value
    if next_regular:
        next_regular.value += bomb.next.value
    new_node = Node(bomb.prev.prev, bomb.next.next.next, 0)
    bomb.prev.prev.next = new_node
    bomb.next.next.next.prev = new_node


def find_bomb(node: Node) -> Optional[Node]:
    depth, current = 0, node
    while current and depth < 5:
        if current.value < 0:
            depth += current.value + 2
        current = current.next
    return current


def find_splittable(node: Node) -> Optional[Node]:
    current = node
    while current and current.value <= 9:
        current = current.next
    return current


def split(node: Node):
    open_bracket = Node(node.prev, None, -1)
    left_number = Node(open_bracket, None, node.value // 2)
    right_number = Node(left_number, None, int(ceil(node.value / 2)))
    closed_bracket = Node(right_number, None, -3)
    node.prev.next = open_bracket
    open_bracket.next = left_number
    left_number.next = right_number
    right_number.next = closed_bracket
    closed_bracket.next = node.next
    node.next.prev = closed_bracket


def add(node: Node, summand: Node) -> Node:
    node.prev = Node(None, node, -1)
    last = find_last(node)
    last.next = summand
    summand.prev = last
    last = find_last(summand)
    last.next = Node(last, None, -3)
    return node.prev


def reduce_node(node: Node):
    while True:
        if bomb := find_bomb(node):
            explode(bomb)
        elif splittable := find_splittable(node):
            split(splittable)
        else:
            break


def add_list(nodes: list[Node]) -> Node:
    remaining = list(nodes)
    node = remaining.pop(0)
    while remaining:
        node = add(node, remaining.pop(0))
        reduce_node(node)
    return node


def remove_right(node: Node):
    if node.prev.prev:
        node.prev.prev.next = node
        node.prev = node.prev.prev
    else:
        node.prev = None


def remove_left(node: Node):
    if node.next.next.next:
        node.next.next.next.prev = node
        node.next = node.next.next.next
    else:
        node.next = None


def calc_magnitude(node: Node) -> int:
    current = node
    while current.next:
        if current.value >= 0 and current.next.value >= 0:
            current.value = 3 * current.value + 2 * current.next.value
            remove_right(current)
            remove_left(current)
            current = node
        else:
            current = current.next
    return current.value


def get_value(char) -> int:
    return -1 if char == '[' else -3 if char == ']' else int(char)


def solve_part_1(nodes: list[Node]) -> int:
    first = add_list(nodes)
    return calc_magnitude(first)


def summands(nodes: list[Node]) -> Iterator[tuple[Node, Node]]:
    for first in nodes:
        for summand in [n for n in nodes if str(first) != str(n)]:
            yield first, summand


def solve_part_2(nodes: list[Node]) -> int:
    max_mag = 0
    for first, summand in summands(nodes):
        node = add(clone_nodes(first), clone_nodes(summand))
        reduce_node(node)
        max_mag = max(max_mag, calc_magnitude(node))
    return max_mag


def parse_chars(chars: str) -> Node:
    first_node = Node(None, None, -1)
    prev = first_node
    for i in range(1, len(chars)):
        prev.next = Node(prev, None, get_value(chars[i]))
        prev = prev.next
    return first_node


def parse_input(lines: list[str]) -> list[Node]:
    return [parse_chars(line.replace(',', '')) for line in lines]


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        lines = fp.read().splitlines()
    return solve_part_1(parse_input(lines)), solve_part_2(parse_input(lines))


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
