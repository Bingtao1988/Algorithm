# Binary Tree:
# 1. Every node has at most two children.
# 2. Each child node is labeled as being either a left child or a right child.
# 3. A left child precedes a right child in the order of children of a node.

# proper binary tree: each node has two or zero child.
class Tree:
    """ Abstract base class representing a tree structure. """
    class Position:
        """An abstraction representing the location of a single element."""
        def element(self):
            """ Return the element stored at this Position. """
            raise NotImplementedError
        def __eq__(self, other):
            """ Return True if other Position represents the same location. """
            raise NotImplementedError
        def __ne__(self, other):
            """ Return True if other does not represent the same location. """
            return not (self == other)

    def root(self):
        """ Return Position representing the tree's root (or None if it's empty)"""
        raise NotImplementedError
    def parent(self, p):
        """ Return Position representing p's parent (or None if p is root) """
        raise NotImplementedError
    def num_children(self, p):
        """ Return the number of children that Position p has. """
        raise NotImplementedError
    def children(self, p):
        """ Generate an iteration of Positions representing p's children. """
        raise NotImplementedError
    def __len__(self):
        """ Return the total number of elements in the tree. """
        raise NotImplementedError
    def is_root(self, p):
        """ Return True if Position p represents the root of the tree. """
        return self.root() == p
    def is_leaf(self, p):
        """ Return True if Position p does not have any children. """
        return self.num_children(p) == 0
    def is_empty(self, p):
        """ Return True if the tree is empty """
        return len(self) == 0


class BinaryTree(Tree):
    """Abstract base class representing a binary tree structure."""
    def left(self, p):
        """ Return a Position representing p's left child
        Return None if p does not have a left child.
        """
        raise NotImplementedError
    def right(self, p):
        """ Return a Position representing p's right child
        Return None if p does not have a right child.
        """
        raise NotImplementedError
    def sibling(self, p):
        """Return a Position representing p's sibling (or None if no Sibling)"""
        parent = self.parent(p)
        if parent == None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        """ Generate an iteration of Positions representing p's children."""
        if self.left(p) != None:
            yield self.left(p)
        if self.right(p) != None:
            yield self.right(p)
