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
