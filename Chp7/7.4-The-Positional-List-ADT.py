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

class PositionalList(_DoublyLinkedBase):
    """ A sequential container of elements allowing positional access. """
    class Position:
        """ An abstraction representing the location of a single element. """

        def __init__(self, container, node):
            """Constructor should not be invoked by user. """
            self._container = container
            self._node = node

        def element(self):
            """ Return the element stored at the Position. """
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return ((type(other) is type(self)) and (other._node is self._node)

        def __ne__(self, other):
            """Return True if other is not a Position representing of this location."""
            return not(self == other)

        def _validate(self, p):
            """ Return position's node, or raise appropriate error if valid. """
            if not isinstance(p, self.Position):
                raise TypeError
            if p._container is not self:
                raise ValueError
            if p._node._next is None:
                raise ValueError
            return p._node

        def _make_position(self, node):
            """ Return Position instance for given node (or None if sentinel)"""
            if node is self._header or node is self._trailer:
                return None
            else:
                return self.Position(self, node)

        def first(self):
            return self._make_position(self._header._next)
        def last(self):
            return self._make_position(self._trailer._prev)
        def before(self, p):
            node = self._validate(p)
            return self._make_position(node._prev)
        def after(self, p):
            node = self._validate(p)
            return self._make_position(node._next)
        def __iter__(self):
            cursor = self.first()
            while cursor is not None:
                yield cursor.element()
                cursor = self.after(cursor)
        def _insert_between(self, e, predecessor, successor):
            node = super()._insert_between(e, predecessor, successor)
            return self._make_position(node)

        def add_first(self, e):
            return self._insert_between(e, self._header, self._header._next)
        def add_last(self, e):
            return self._insert_between(e, self._trailer._prev, self._trailer)

        def add_before(self, p, e):
            original = self._validate(p)
            return self._insert_between(e, original._prev, original)

        def add_after(self, p, e):
            original = self._validate(p)
            return self._insert_between(e, original, original._next)
        def delete(self, p):
            original = self._validate(p)
            return self._delete_node(original)

        def replace(self, p, e):
            original = self._validate(p)
            old_value = original._element
            original._element = e
            return old_value
