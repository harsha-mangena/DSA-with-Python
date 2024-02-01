class Stack:
    def __init__(self, max_elements=0):
        # Initialize the stack with a fixed maximum size.
        self.max_elements = max_elements
        self._initialize_stack()

    def _initialize_stack(self):
        # Create a list of 'None' elements with a size equal to max_elements.
        # Initially, the stack size is 0.
        self.stack = [None] * self.max_elements
        self.size = 0

    def push(self, data):
        # Add an element to the top of the stack.
        # If the stack is full, raise an exception.
        if self.size >= self.max_elements:
            raise Exception("Stack is full")
        self.stack[self.size] = data
        self.size += 1

    def pop(self):
        # Remove the top element of the stack.
        # If the stack is empty, raise an exception.
        if self.size == 0:
            raise Exception("Stack is empty")
        self.size -= 1
        self.stack[self.size] = None

    def peek(self):
        # Return the top element of the stack without removing it.
        # If the stack is empty, raise an exception.
        if self.size == 0:
            raise Exception("Stack is empty")
        return self.stack[self.size - 1]

    def is_empty(self):
        # Check if the stack is empty.
        return self.size == 0

    def display(self):
        # Display the elements in the stack.
        if self.size == 0:
            print("[]")
        else:
            for i in range(self.size):
                print(self.stack[i], end=" ")
            print()


# Demonstration of Stack functionality
s = Stack(max_elements=10)

s.push(10)  # Stack after push(10): [10, None, None, ..., None]
s.push(11)  # Stack after push(11): [10, 11, None, ..., None]
s.display()  # Output: 10 11

s.pop()  # Stack after pop(): [10, None, None, ..., None]
s.display()  # Output: 10

s.pop()  # Stack after pop(): [None, None, None, ..., None]
s.display()  # Output: []
