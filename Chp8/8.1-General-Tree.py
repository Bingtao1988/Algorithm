# Tree is an organizational relationship that is richer than the simple "before"
# and "after" relationships between objects in sequences.

# We define a tree T as a set of nodes storing elements such that the nodes have
# a parent-child relationship that satisfies the following properties:
# 1. If T is nonempty, it has a special node, called the root of T, that has no parent
# 2. Each node v of T different from the root has a unique parent node w; every
#    node with parent w is a child of w.

# Two nodes that are children of the same parent are siblings.
# A node v is external if v has no children.
# A node v is internal if it has one or more children.

# Ancestor
# Descendant

# edge: A pair of two nodes
# path: A sequence of nodes such that any two consecutive nodes in the sequence
#       form an edge.

# A tree is ordered if there is a meaningful linear order among the children of
# each node. -- Ordered Tree

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
        
