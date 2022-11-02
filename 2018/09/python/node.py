from dataclasses import dataclass
from typing import Optional, Self


@dataclass
class Node:
    value: int
    right: Optional[Self] = None
    left: Optional[Self] = None

    def insert(self, value: int) -> Self:
        new_node = Node(value, left=self, right=self.right)
        self.right.left = new_node
        self.right = new_node
        return new_node

    def remove(self) -> Self:
        next_node = self.right
        self.left.right = self.right
        self.right.left = self.left
        self.left = None
        self.right = None
        return next_node

    def go_right(self, distance: int) -> Self:
        node = self
        for i in range(distance):
            node = node.right
        return node

    def go_left(self, distance: int) -> Self:
        node = self
        for i in range(distance):
            node = node.left
        return node
