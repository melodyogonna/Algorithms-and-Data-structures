import unittest

from stack import Stack


class StackTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.stack = Stack()

    def test_empty_stack(self):
        self.assertEqual(self.stack.is_empty(), True)

    def test_non_empty_stack(self):
        self.stack.push(10)
        self.assertEqual(self.stack.is_empty(), False)

    def test_peek(self):
        self.stack.push(10)
        self.assertEqual(self.stack.peek(), 10)

    def test_push(self):
        self.stack.push(2)
        self.stack.push(30)
        self.stack.push(5)
        self.assertEqual(self.stack.peek(), 5)

    def test_pop(self):
        self.stack.push(2)
        self.stack.push(30)
        self.stack.push(5)
        self.assertEqual(self.stack.pop(), 5)
        self.assertEqual(self.stack.pop(), 30)
        self.assertEqual(self.stack.pop(), 2)

if __name__ == '__main__':
    unittest.main()
