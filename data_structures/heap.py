class MinIntHeap:
    def __init__(self):
        self.tree_array: list[int] = []
        self.size = 0

    def _get_left_index(self, parent_index: int) -> int:
        return (parent_index * 2) + 1

    def _get_right_index(self, parent_index: int) -> int:
        return (parent_index * 2) + 2

    def _get_parent_index(self, child_index: int) -> int:
        return int((child_index - 1) / 2)

    def _get_left_child(self, parent_index: int):
        return self.tree_array[self._get_left_index(parent_index)]

    def _get_right_child(self, parent_index: int) -> int:
        return self.tree_array[self._get_right_index(parent_index)]

    def _get_parent(self, child_index: int) -> int:
        return self.tree_array[self._get_parent_index(child_index)]

    def _has_left_child(self, parent_index: int) -> bool:
        return self._get_left_child(parent_index) < self.size

    def _has_right_child(self, parent_index: int) -> bool:
        return self._get_right_child(parent_index) < self.size

    def _has_parent(self, child_index: int) -> bool:
        return self._get_parent(child_index) >= 0

    def _swap(self, first_index, second_index) -> None:
        temp = self.tree_array[first_index]
        self.tree_array[first_index] = self.tree_array[second_index]
        self.tree_array[second_index] = temp


    def peek(self):
        return self.tree_array[0]