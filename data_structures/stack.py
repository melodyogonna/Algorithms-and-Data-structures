from typing import Union

class Stack:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next: Union[Stack.Node, None] = None

    def __init__(self):
        self.top: Union[Stack.Node, None] = None

    def is_empty(self) -> bool:
        return self.top is None

    def peek(self):
        return self.top.data

    def push(self, data):
        new_node = self.Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        data = self.top.data
        self.top = self.top.next
        return data


