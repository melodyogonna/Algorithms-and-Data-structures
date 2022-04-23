import unittest

from linked_list import LinkedList

class TestLinkedList(unittest.TestCase):
    def setUp(self) -> None:
        self.linked_list = LinkedList()

    def test_linked_list_instanciated(self):
        self.assertIsInstance(self.linked_list, LinkedList)

    def test_linked_list_append(self):
        self.linked_list.append(10)
        self.assertIsNotNone(self.linked_list.head)
        self.assertEqual(10, self.linked_list.head.data)

    def test_prepend(self):
        self.linked_list.append(10)
        self.linked_list.append(25)
        self.linked_list.prepend(5)
        self.assertEqual(self.linked_list.head.data, 5)

    def test_search(self):
        self.linked_list.append(10)
        self.linked_list.append(20)
        self.linked_list.append(50)
        self.assertIsNotNone(self.linked_list.search(50))
        self.assertIsNone(self.linked_list.search(30))

    def test_delete(self):
        self.linked_list.append(10)
        self.linked_list.append(20)
        self.linked_list.append(50)
        self.linked_list.append(70)
        self.linked_list.delete(20)
        self.assertIsNone(self.linked_list.search(20))


if __name__ == '__main__':
    unittest.main()
