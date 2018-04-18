from binary_tree import BinaryTree

class LinkedBinaryTree(BinaryTree):
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
    class Position(BinaryTree.Position):
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

    #-------------------------- public mutators --------------------------
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

    def replace(self, p, e):
        """Replace the element at position p with e, and return old element."""
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def delete(self, p):
        """Delete the node at Position p, and replace it with its child, if any.

        Return the element that had been stored at Position p.
        Raise ValueError if Position p is invalid or p has two children.
        """
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError('Position has two children')
        child = node._left if node._left else node._right  # might be None
        if child is not None:
            child._parent = node._parent   # child's grandparent becomes parent
        if node is self._root:
            self._root = child             # child becomes root
        else:
            parent = node._parent
        if node is parent._left:
            parent._left = child
        else:
            parent._right = child
        self._size -= 1
        node._parent = node              # convention for deprecated node
        return node._element
  
    def attach(self, p, t1, t2):
        """Attach trees t1 and t2, respectively, as the left and right subtrees of the external Position p.

        As a side effect, set t1 and t2 to empty.
        Raise TypeError if trees t1 and t2 do not match type of this tree.
        Raise ValueError if Position p is invalid or not external.
        """
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError('position must be leaf')
        if not type(self) is type(t1) is type(t2):    # all 3 trees must be same type
            raise TypeError('Tree types must match')
        self._size += len(t1) + len(t2)
        if not t1.is_empty():         # attached t1 as left subtree of node
            t1._root._parent = node
            node._left = t1._root
            t1._root = None             # set t1 instance to empty
            t1._size = 0
        if not t2.is_empty():         # attached t2 as right subtree of node
            t2._root._parent = node
            node._right = t2._root
            t2._root = None             # set t2 instance to empty
            t2._size = 0


    def flip(self,p):
        ''' flips the left and right children of position p '''
        ############################ Task 6 flip ###############################
        pass
	
    def flip_subtree(self,p=None):
        '''flips the left and right children all nodes in the subtree of p, 
        and if p is omitted it flips the entire tree'''
        ############################ Task 7 flip ###############################
        pass

    def return_max(self, p=None):
        '''Traverse the tree and return the maximum value stored within the tree.'''
        ############################ Task 8 return_max ###############################
        pass


    def pretty_print(self):
        levels = self.height() + 1
        self._print_internal([self._root], 1, levels)

    def _print_internal(self, this_level_nodes, current_level, max_level):
        if (len(this_level_nodes) == 0 or all_elements_are_None(this_level_nodes)):
            return  # Base case of recursion: out of nodes, or only None left

        floor = max_level - current_level;
        endgeLines = 2 ** max(floor - 1, 0);
        firstSpaces = 2 ** floor - 1;
        betweenSpaces = 2 ** (floor + 1) - 1;
        print_spaces(firstSpaces)
        next_level_nodes = []
        for node in this_level_nodes:
            if (node is not None):
                print(node._element, end = "")
                next_level_nodes.append(node._left)
                next_level_nodes.append(node._right)
            else:
                next_level_nodes.append(None)
                next_level_nodes.append(None)
                print_spaces(1)

            print_spaces(betweenSpaces)
        print()
        for i in range(1, endgeLines + 1):
            for j in range(0, len(this_level_nodes)):
                print_spaces(firstSpaces - i)
                if (this_level_nodes[j] == None):
                    print_spaces(endgeLines + endgeLines + i + 1);
                    continue
                if (this_level_nodes[j]._left != None):
                    print("/", end = "")
                else:
                    print_spaces(1)
                print_spaces(i + i - 1)
                if (this_level_nodes[j]._right != None):
                    print("\\", end = "")
                else:
                    print_spaces(1)
                print_spaces(endgeLines + endgeLines - i)
            print()

        self._print_internal(next_level_nodes, current_level + 1, max_level)


	
def all_elements_are_None(list_of_nodes):
    for each in list_of_nodes:
        if each is not None:
            return False
    return True

def print_spaces(number):
    for i in range(number):
        print(" ", end = "")
        




def main():

    ###################### Draws sample tree 1 #######################

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
    T1.pretty_print()

    ###################### End of Drawing sample tree 1 #####################



    ############################ Task 3 draw a tree ###############################
    T = LinkedBinaryTree()
	
    # Your code to construct tree in task 3
    ancestor = T.add_root("ancestor")
    grandfather = T.add_left(ancestor,"gf")
    T.add_left(grandfather,"f")
    T.add_right(grandfather,"m")
    grandmother = T.add_right(ancestor,"gm")
    T.add_left(grandmother,"u")
    T.add_right(grandmother,"a")
    
    
	
    T.pretty_print() # Shows your tree


	
    ############################ Task 4 depth ###############################

    print("Depth of T1's root: ",T1.depth(T1.root())) # Should print 0
    print("Depth of T1's x5: ",T1.depth(x5))   # Should print 3
    print("Depth of T1's x6: ",T1.depth(x6))   # Should print 4

    ############################ Task 5 tree traversal ###############################
    print("Displaying pre order traversal ...")
    T1.preorderPrint(T1.root())  # Answer: A B C E F D G 1 2 3 4 5 6
    print("\n\n")
    print("Displaying post order traversal ...")
    T1.postorderPrint(T1.root()) # Answer: E F C G D B 2 4 6 5 3 1 A
    print("\n\n")
    print("Displaying in order traversal ...")  
    T1.inorderPrint(T1.root())  # Answer: E C F B G D A 2 1 4 3 6 5
    print("\n\n")
    print("Displaying level order traversal ...")   
    T1.levelorderPrint(T1.root())   # Answer: A B 1 C D 2 3 E F G 4 5 6


    ############################ Task 6,7 flip ###############################

    #print("After flipping root node")
    #T1.flip(T1.root())   # Flipping around root
    #T1.pretty_print()
    #print("After flipping the entire subtree")
    #T1.flip_subtree()    # Every subtree should be flipped
    #T1.pretty_print()

    ############################ Task 8 return_max ###############################
    #print("Testing return_max...")
    #print("Maximum of your task 3's tree is", T.return_max()) # Should be 8

main()

     

 





