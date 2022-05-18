from typing import Union


class Queue:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head: Union[Queue.Node, None] = None
        self.tail: Union[Queue.Node, None] = None

    @property
    def is_empty(self) -> bool:
        return self.head is None

    def add(self, data):
        node = self.Node(data)

        if self.tail is not None:
            self.tail.next = node
        self.tail = node

        if self.head is None:
            self.head = node

    def remove(self):
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return data
