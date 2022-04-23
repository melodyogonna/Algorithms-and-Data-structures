class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

    def __str__(self):
        print(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(data)
        return

    def prepend(self, data):
        new_head = Node(data)

        if self.head is None:
            self.head = new_head
            return

        new_head.next = self.head
        self.head = new_head
        return

    def delete(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            if self.head.next is not None:
                self.head = self.head.next
            else:
                self.head = None
            return

        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            else:
                current = current.next

    def search(self, data):
        if self.head is None:
            return None

        current = self.head
        while current.next is not None:
            if current.data == data:
                return current
            else:
                current = current.next

        return None
