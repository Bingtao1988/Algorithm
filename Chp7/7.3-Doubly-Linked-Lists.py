# We cannot efficiently delete an arbitrary node from an interior position of
# the list if only given a reference to that node, because we cannot determine
# the node that immediately precedes the node to be deleted.

# Advantage of sentinels:
# 1. the header and trailer nodes never change.
# 2. all insertions is in a unified manner.

class _DoublyLinkedBase:
    """ A base class providing a doubly linked list representation."""
    class _Node:
        """Lightweight, nonpublic class for storing a doubly linked node. """
        __slot__ == '_element', "_prev", "_next"
        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        """ Create an empty list. """
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        """ Return the number of elements in the list. """
        return self._size

    def is_empty(self):
        """ Return True if list is empty. """
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """ Add element e between two existing nodes and return new node. """
        newest = _Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, e):
        """ Delete nonsentinel node from the list and return its element. """
        predecessor = e._prev
        successor = e._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = e._element
        e._prev = e._next = e_element = None
        return element

class LinkedDeque(_DoublyLinkedBase):
    def first(self):
        """ Return (but do not remove) the element at the front of the deque"""
        if self.is_empty():
            raise IndexError
        element = self._header._next._element
        return element
    def last(self):
        """ Return (but do not remove) the element at the end of the deque """
        if self.is_empty():
            raise IndexError
        element = self._trailer._prev._element
        return element

    def insert_first(e, self):
        """ Add an element to the front of the deque """
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        """ Add an element to the front of the deque """
        self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self, e):
        """ Remove and return the element from the front of the deque.
        Raise IndexError if the deque is empty. """
        if self.is_empty():
            raise IndexError
        return self._delete_node(self._header._next)

    def delete_last(self, e):
        """ Remove and return the element from the endof the deque.
        Raise IndexError if the deque is empty. """
        if self.is_empty():
            raise IndexError
        return self._delete_node(self._trailer._prev)
