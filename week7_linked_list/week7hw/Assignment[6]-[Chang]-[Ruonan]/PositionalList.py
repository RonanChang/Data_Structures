class _DoublyLinkedBase:
    """A base class providing a doubly linked list representation."""

    #-------------------------- nested _Node class --------------------------
    # nested _Node class
    class _Node:
        """Lightweight, nonpublic class for storing a doubly linked node."""
        __slots__ = '_element', '_prev', '_next'            # streamline memory

        def __init__(self, element, prev, next):            # initialize node's fields
            self._element = element                           # user's element
            self._prev = prev                                 # previous node reference
            self._next = next                                 # next node reference

	#-------------------------- list constructor --------------------------

    def __init__(self):
        """Create an empty list."""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer                  # trailer is after header
        self._trailer._prev = self._header                  # header is before trailer
        self._size = 0                                      # number of elements

	#-------------------------- public accessors --------------------------

    def __len__(self):
        """Return the number of elements in the list."""
        return self._size

    def is_empty(self):
        """Return True if list is empty."""
        return self._size == 0

	#-------------------------- nonpublic utilities --------------------------

    def _insert_between(self, e, predecessor, successor):
        """Add element e between two existing nodes and return new node."""
        newest = self._Node(e, predecessor, successor)      # linked to neighbors
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        """Delete nonsentinel node from the list and return its element."""
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element                             # record deleted element
        node._prev = node._next = node._element = None      # deprecate node
        return element                                      # return deleted element


class PositionalList(_DoublyLinkedBase):
    """A sequential container of elements allowing positional access."""

    #-------------------------- nested Position class --------------------------
    class Position:
        """An abstraction representing the location of a single element.

        Note that two position instaces may represent the same inherent
        location in the list.  Therefore, users should always rely on
        syntax 'p == q' rather than 'p is q' when testing equivalence of
        positions.
        """

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

        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not (self == other)               # opposite of __eq__
		
        #------------------------------- utility methods -------------------------------
    def _validate(self, p):
        """Return position's node, or raise appropriate error if invalid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:                  # convention for deprecated nodes
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node (or None if sentinel)."""
        if node is self._header or node is self._trailer:
            return None                              # boundary violation
        else:
            return self.Position(self, node)         # legitimate position
		
    #------------------------------- accessors -------------------------------
    def first(self):
        """Return the first Position in the list (or None if list is empty)."""
        return self._make_position(self._header._next)

    def last(self):
        """Return the last Position in the list (or None if list is empty)."""
        return self._make_position(self._trailer._prev)

    def before(self, p):
        """Return the Position just before Position p (or None if p is first)."""
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        """Return the Position just after Position p (or None if p is last)."""
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        """Generate a forward iteration of the elements of the list."""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

	#------------------------------- mutators -------------------------------
	# override inherited version to return Position, rather than Node
    def _insert_between(self, e, predecessor, successor):
        """Add element between existing nodes and return new Position."""
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        """Insert element e at the front of the list and return new Position."""
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        """Insert element e at the back of the list and return new Position."""
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        """Insert element e into list before Position p and return new Position."""
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        """Insert element e into list after Position p and return new Position."""
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        """Remove and return the element at Position p."""
        original = self._validate(p)
        return self._delete_node(original)  # inherited method returns element

    def replace(self, p, e):
        """Replace the element at Position p with e.

        Return the element formerly at Position p.
        """
        original = self._validate(p)
        old_value = original._element       # temporarily store old element
        original._element = e               # replace with new element
        return old_value                    # return the old element value

    def __str__(self):
        result = []
        result.append("Head <--> ")
        for each in self:
            result.append(str(each) + " <--> ")
        result.append("Tail")
        return "".join(result)

    def split_after_position(self, p):
        
        # Splits self list into two lists. After splitting, the self list will include
        # things up to and include p. return another valid PositionalList that contains things after p.
        # This function should run O(1)
        # No need to consider size, or you can adjust size in O(n)
        # @parameter1: p, Position of splitting node.
        # @return: a new PositionalList, containing things after p
        # 
        # Example:
        # self list: head <--> 5 <--> 3 <--> 2 <--> 1 <--> tail
        # p is Position of 3's node
        # >>> l.split_after_position(p)
        # Should return 				head <--> 2 <--> 1 <--> tail
        # self list should become		head <--> 5 <--> 3 <--> tail

        # To do
        new_list = PositionalList()
        position = self.after(p)
        while True:
            if position is None:
                break
            next_position = self.after(position)
            new_list.add_last(self.delete(position))
            position = next_position
        return new_list

def play():
    # task 1, play around Positional List class.
    # 1. start an instance of Positional List
    # 2. insert value 9999, make 9999 the first node, save the Position of 9999 in a variable.
    # 3. insert value 6666 after 9999, save the Position of 6666 in a variable.
    # 4. replace value 6666 with 66666. 
    # 5. delete 9999.
    
    myList = PositionalList()
    print(myList)
    pos1 = myList.add_first(9999)
    print(myList)
    pos2 = myList.add_after(pos1, 6666)
    print(myList)
    myList.replace(pos2, 66666)
    print(myList)
    myList.delete(pos1)
    print(myList)
    
        
play()

split_after_position_test = True

if (split_after_position_test):
    print("-----------Testing split_after_position-------------")
    l1 = PositionalList()
    l1.add_last(5)
    position_for_three = l1.add_last(3)
    l1.add_last(2)
    l1.add_last(1)
    print(l1)  # Head <--> 5 <--> 3 <--> 2 <--> 1 <--> Tail
    l2 = l1.split_after_position(position_for_three)
    print(l1)  # Head <--> 5 <--> 3 <--> Tail
    print(l2)  # Head <--> 2 <--> 1 <--> Tail

