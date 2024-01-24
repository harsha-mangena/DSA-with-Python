class Node:
    """A node in the linked list."""

    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    """A singly linked list."""

    def __init__(self):
        self.head = None

    def _create_new_node(self, data) -> Node:
        """Creates a new Node."""
        return Node(data)

    def insert_at_beginning(self, data) -> None:
        """Inserts a new node at the beginning of the linked list."""
        node = self._create_new_node(data)
        node.next = self.head
        self.head = node

    def append(self, data) -> None:
        """Appends a new node at the end of the linked list."""
        node = self._create_new_node(data)
        if self.head is None:
            self.head = node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = node

    def display(self) -> None:
        """Displays the contents of the linked list."""
        if not self.head:
            print("Linked List is empty")
            return

        current = self.head
        while current:
            print(current.data, "->", end=" ")
            current = current.next
        print("None")

    def delete(self, data) -> bool:
        """Deletes a node with the given data. Returns True if deletion is successful."""
        if not self.head:
            print("Linked List is empty")
            return False

        if self.head.data == data:
            self.head = self.head.next
            return True

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return True
            current = current.next

        print("Data not found")
        return False

    def clear(self) -> None:
        """Clears the linked list."""
        self.head = None

    def length(self) -> int:
        """Returns the number of nodes in the linked list."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
