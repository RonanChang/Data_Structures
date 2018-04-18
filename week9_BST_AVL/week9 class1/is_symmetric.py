class LinkedBinaryTree():
    """Linked representation of a binary tree structure."""

    #-------------------------- nested _Node class --------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a node."""
        __slots__ = '_element', '_parent', '_left', '_right' # streamline memory usage

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    #-------------------------- nested Position class --------------------------
    class Position():
        """An abstraction representing the location of a single element."""

        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this Position."""
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node

    #------------------------------- utility methods -------------------------------
    def _validate(self, p):
        """Return associated node, if position is valid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:      # convention for deprecated nodes
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node (or None if no node)."""
        return self.Position(self, node) if node is not None else None

    def sibling(self, p):
        """Return a Position representing p's sibling (or None if no sibling)."""
        parent = self.parent(p)
        if parent is None:                    # p must be the root
            return None                         # root has no sibling
        else:
            if p == self.left(parent):
                return self.right(parent)         # possibly None
            else:
                return self.left(parent)          # possibly None

    #------------------------------- binary_tree methods -------------------------------

    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    def inorder(self):
        """Generate an inorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_inorder(self, p):
        """Generate an inorder iteration of positions in subtree rooted at p."""
        if self.left(p) is not None:          # if left child exists, traverse its subtree
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p                               # visit p between its subtrees
        if self.right(p) is not None:         # if right child exists, traverse its subtree
            for other in self._subtree_inorder(self.right(p)):
                yield other

    # override inherited version to make inorder the default
    def positions(self):
        """Generate an iteration of the tree's positions."""
        return self.inorder()    

    def is_root(self, p):
        """Return True if Position p represents the root of the tree."""
        return self.root() == p

    def is_leaf(self, p):
        """Return True if Position p does not have any children."""
        return self.num_children(p) == 0

    def is_empty(self):
        """Return True if the tree is empty."""
        return len(self) == 0 

    def _height2(self, p):                  # time is linear in size of subtree
        """Return the height of the subtree rooted at Position p."""
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p=None):
        """Return the height of the subtree rooted at Position p.

        If p is None, return the height of the entire tree.
        """
        if p is None:
            p = self.root()
        return self._height2(p)        # start _height2 recursion   

    #-------------------------- binary tree constructor --------------------------
    def __init__(self):
        """Create an initially empty binary tree."""
        self._root = None
        self._size = 0

    #-------------------------- public accessors --------------------------
    def __len__(self):
        """Return the total number of elements in the tree."""
        return self._size
    
    def root(self):
        """Return the root Position of the tree (or None if tree is empty)."""
        return self._make_position(self._root)

    def parent(self, p):
        """Return the Position of p's parent (or None if p is root)."""
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        """Return the Position of p's left child (or None if no left child)."""
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        """Return the Position of p's right child (or None if no right child)."""
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        """Return the number of children of Position p."""
        node = self._validate(p)
        count = 0
        if node._left is not None:     # left child exists
            count += 1
        if node._right is not None:    # right child exists
            count += 1
        return count
    
    def add_root(self, e):
        """Place element e at the root of an empty tree and return new Position.

        Raise ValueError if tree nonempty.
        """
        if self._root is not None:
            raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def add_left(self, p, e):
        """Create a new left child for Position p, storing element e.

        Return the Position of new node.
        Raise ValueError if Position p is invalid or p already has a left child.
        """
        node = self._validate(p)
        if node._left is not None:
            raise ValueError('Left child exists')
        self._size += 1
        node._left = self._Node(e, node)                  # node is its parent
        return self._make_position(node._left)

    def add_right(self, p, e):
        """Create a new right child for Position p, storing element e.

        Return the Position of new node.
        Raise ValueError if Position p is invalid or p already has a right child.
        """
        node = self._validate(p)
        if node._right is not None:
            raise ValueError('Right child exists')
        self._size += 1
        node._right = self._Node(e, node)                 # node is its parent
        return self._make_position(node._right)


    def is_symmetric(self, p):
        '''returns True if the tree is symmetric, returns False otherwise.'''
        # You may find examples in main()
        return self.is_symmetric_inner(self.left(p), self.right(p))
    
    def is_symmetric_inner(self, left, right):
        # Hint: recursion!
        # Hint2: Handle None case
        # To do
        if (self.children(left) is None) and (self.children(right) is None):            
            self.is_symmetric_inner(self.left(left),self.right(right))
            self.is_symmetric_inner(self.right(left),self.left(right))
        
        return left.element() == right.element()


def main():

    ###################### Generate sample tree #######################
#               A                               
#              / \               
#             /   \              
#            /     \             
#           /       \            
#          /         \           
#         /           \          
#        /             \         
#       /               \        
#       B               1               
#      / \             / \       
#     /   \           /   \      
#    /     \         /     \     
#   /       \       /       \    
#   C       D       2       3       
#  / \     /               / \   
# /   \   /               /   \  
# E   F   G               4   5   
#                            /   
#                            6   
                                          
    T1 = LinkedBinaryTree()
    a = T1.add_root("A")
    b = T1.add_left(a,"B")
    c = T1.add_left(b,"C")
    d = T1.add_right(b,"D")
    T1.add_left(c,"E")
    T1.add_right(c,"F")
    T1.add_left(d,"G")
    x1 = T1.add_right(a,"1")
    T1.add_left(x1,"2")
    x3 = T1.add_right(x1,"3")
    T1.add_left(x3,"4")
    x5 = T1.add_right(x3,"5")
    x6 = T1.add_left(x5,"6")
    print(T1.is_symmetric(T1.root()))     # False, because tree above is not symmetric
    
#   1       
#  / \   
# /   \  
# 2   2   
#/ \ / \ 
#3 4 4 3 
    
    T3 = LinkedBinaryTree()
    x11 = T3.add_root(1)
    x21 = T3.add_left(x11,2)
    x22 = T3.add_right(x11,2)
    x31 = T3.add_left(x21,3)
    x32 = T3.add_right(x21,4)
    x33 = T3.add_left(x22,4)
    x34 = T3.add_right(x22,3)
    print(T3.is_symmetric(T3.root()))  # True, because tree above is symmetric
main()