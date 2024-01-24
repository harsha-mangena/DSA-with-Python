# LinkedList Implementation

## Contents
- [Node Class](#node-class)
- [LinkedList Class](#linkedlist-class)
- [Usage](#usage)
- [Real-Life Applications](#real-life-applications)
- [Testing](#testing)

## Node Class

The `Node` class is a simple structure with two attributes:
- `data`: Holds the value stored in the node.
- `next`: Points to the next node in the list, or `None` if it is the last node.

## LinkedList Class

The `LinkedList` class provides several methods to work with linked lists:
- `insert_at_beginning`: Adds a new node at the start of the list.
- `append`: Adds a new node at the end of the list.
- `display`: Prints out the entire list.
- `delete`: Removes a node with a specific value.
- `clear`: Clears the entire list.
- `length`: Returns the number of nodes in the list.

## Usage

Here's a simple example of how to use the LinkedList class:

```python
ll = LinkedList()
ll.insert_at_beginning(10)
ll.append(20)
ll.display()  # Output: 10 -> 20 -> None
```

## Usecases
`LinkedLists` are fundamental data structures used in various real-world applications.

* **Dynamic Memory Allocation**: Used to manage blocks of memory dynamically.
* **Implementing Stacks and Queues**: Particularly useful in applications where the data structure needs to frequently grow and shrink.
* **Music Playlists**: For enabling easy addition and removal of songs.
* **Undo Functionality in Applications**: Storing previous states in an application to allow undo operations.