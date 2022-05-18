import unittest

from queue import Queue


class QueueTest(unittest.TestCase):
    def setUp(self) -> None:
        self.queue = Queue()

    def test_queue_is_empty(self):
        self.assertEqual(self.queue.is_empty, True)

    def test_queue_is_not_empty(self):
        self.queue.add(29)
        self.assertEqual(self.queue.is_empty, False)

    def test_data_is_added(self):
        data = 'my data haha'
        self.queue.add(data)
        self.assertEqual(self.queue.head.data, data)

    def test_tail_is_added(self):
        first_data = 'my_first_data'
        second_data = 'my_second_data'
        self.queue.add(first_data)
        self.queue.add(second_data)
        self.assertEqual(self.queue.tail.data, second_data)

    def test_head_is_retrieved(self):
        first_data = 'my_first_data'
        second_data = 'my_second_data'
        third_data = 'my_third_data'
        self.queue.add(first_data)
        self.queue.add(second_data)
        self.queue.add(third_data)
        self.assertEqual(self.queue.remove(), first_data)
        self.assertEqual(self.queue.remove(), second_data)
        self.assertEqual(self.queue.remove(), third_data)


if __name__ == '__main__':
    unittest.main()
