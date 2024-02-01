import unittest
from stack import Stack


class TestStack(unittest.TestCase):
    def test_push(self):
        stack = Stack(10)
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.size, 2)
        self.assertEqual(stack.peek(), 2)

    def test_pop(self):
        stack = Stack(10)
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.peek(), 2)
        stack.pop()
        self.assertEqual(stack.peek(), 1)

    def test_peek(self):
        stack = Stack(5)
        stack.push("a")
        self.assertEqual(stack.peek(), "a")
        stack.pop()
        self.assertTrue(stack.is_empty())

