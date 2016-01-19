# The tail of the list uses its next reference to point back to the head of the
# list.
class CircularQueue:
    """Queue implementation using circular linked list for storage."""

    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slot__ = '_element', '_next'
        def __init__(self, element, next):
            self._element = element
            self._next = next
    def __init__(self):
        """Create an empty queue."""
        self._tail = None
        self._size = 0
    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size
    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0
    def first(self):
        """Return(but do not remove) the element at the front of the queue.
        Raise IndexError if the queue is empty"""
        if self.is_empty():
            raise IndexError
        head = self._tail._next
        return head._element

    def dequeue(self):
        if self.is_empty():
            raise IndexError
        oldhead = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail = oldhead._next
        self._size -= 1
        return oldhead._element

    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1


    def rotate(self):
        """Rotate front element to the back of the queue."""
        if self._size > 0:
            self._tail = self._tail._next
