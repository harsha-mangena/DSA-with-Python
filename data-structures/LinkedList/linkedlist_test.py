import unittest
from linkedlist import LinkedList  # Replace with the actual module name


class TestLinkedList(unittest.TestCase):

    def test_insert_at_beginning(self):
        ll = LinkedList()
        ll.insert_at_beginning(10)
        self.assertEqual(ll.head.data, 10)
        ll.insert_at_beginning(20)
        self.assertEqual(ll.head.data, 20)

    def test_append(self):
        ll = LinkedList()
        ll.append(30)
        self.assertEqual(ll.head.data, 30)
        ll.append(40)
        ll.append(50)
        self.assertEqual(ll.head.next.next.data, 50)

    def test_delete(self):
        ll = LinkedList()
        ll.append(70)
        ll.append(80)
        ll.delete(70)
        self.assertEqual(ll.head.data, 80)

        result = ll.delete(90)
        self.assertFalse(result)

    def test_clear(self):
        ll = LinkedList()
        ll.append(100)
        ll.append(110)
        ll.clear()
        self.assertIsNone(ll.head)

    def test_length(self):
        ll = LinkedList()
        self.assertEqual(ll.length(), 0)
        ll.append(120)
        ll.append(130)
        self.assertEqual(ll.length(), 2)

if __name__ == '__main__':
    unittest.main()
