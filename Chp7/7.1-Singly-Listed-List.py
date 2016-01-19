# A linked list, relies on a more distributed representation in which a
# lightweight object, known as a node, is allocated for each element. each
# node maintains a reference to its element and one or more references to
# neighboring nodes in order to collectively represent the linear order of the
# sequence.

# Linked list cannot be accessed using a numeric index.

# head --> Start
# tail --> None
# from head to tail --> traversing

# It is really hard to delete the last element in singly linked list since
# when we reach the last element, we cannot go back and fetch the element before
# the last one.

class LinkedStack:
    """LIFO Stack implementation using a singly linked list for storage"""

    #--------------- nested _Node class ------------------#

    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slot__ = '_element', '_next'
        def __init__(self, element, next):
            self._element = element
            self._next = next

    #--------------- Stack methods -----------------------#

    def __init__(self):
        """Create an empty stack."""
        self._head = None
        self._size = 0

    def __len__(self):
        """Return the number of elements in the stack"""
        return self._size

    def is_empty(self):
        """Return true if the stack is empty"""
        return self._size == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        self._head = _Node(e, self._head)
        self._size += 1

    def top(self):
        """Return (but do not remove) the element at the top of the stack.
        Raise IndexError exception if the stack is empty."""
        if self.is_empty():
            raise IndexError
        return self._head._element

    def pop(self):
        """Remove and return the element from the top of the stack
        Raise IndexError exception if the stack is empty"""

        if self.is_empty():
            raise IndexError
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer



class LinkedQueue:
    """FIFO queue implementation using a singly linked list for storage."""

    class _Node:
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise IndexError
        return self._head._element

    def dequeue(self):
        if self.is_empty():
            raise IndexError
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
