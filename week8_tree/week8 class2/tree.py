import collections

class Tree:
    """Abstract base class representing a tree structure."""

    #------------------------------- nested Position class -------------------------------
    class Position:
        """An abstraction representing the location of a single element within a tree.

        Note that two position instaces may represent the same inherent location in a tree.
        Therefore, users should always rely on syntax 'p == q' rather than 'p is q' when testing
        equivalence of positions.
        """

        def element(self):
            """Return the element stored at this Position."""
            raise NotImplementedError('must be implemented by subclass')
			
        def __eq__(self, other):
            """Return True if other Position represents the same location."""
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not (self == other)            # opposite of __eq__

    # ---------- abstract methods that concrete subclass must support ----------
    def root(self):
        
        """Return Position representing the tree's root (or None if empty)."""
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p):
        """Return Position representing p's parent (or None if p is root)."""
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        """Return the number of children that Position p has."""
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        """Return the total number of elements in the tree."""
        raise NotImplementedError('must be implemented by subclass')

    # ---------- concrete methods implemented in this class ----------
    def is_root(self, p):
        """Return True if Position p represents the root of the tree."""
        return self.root() == p

    def is_leaf(self, p):
        """Return True if Position p does not have any children."""
        return self.num_children(p) == 0

    def is_empty(self):
        """Return True if the tree is empty."""
        return len(self) == 0

    def depth(self, p):
        """Return the number of levels separating Position p from the root."""
        ############################ Task 4 depth ###############################
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    
    def height2(self, p):                  
        if self.is_leaf(p):
          return 0
        else:
          return 1 + max(self.height2(c) for c in self.children(p))
    
    def height(self, p=None):
        """Return the height of the subtree rooted at Position p.

        If p is None, return the height of the entire tree.
        """
        ############################ Task 1 height ###############################      
        if p is None:
            p = self.root()
        return self.height2(p)
              

    def __iter__(self):
        """Generate an iteration of the tree's elements."""
        for p in self.positions():                        # use same order as positions()
            yield p.element()                               # but yield each element

    def positions(self):
        """Generate an iteration of the tree's positions."""
        #return self.preorder()                            # return entire preorder iteration
        raise NotImplementedError('must be implemented by subclass')
		