class SingleLinkedList:

    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'         # streamline memory usage

        def __init__(self, element, next):      # initialize node's fields
            self._element = element               # reference to user's element
            self._next = next                     # reference to next node



    def __init__(self):
        """Create an empty linkedlist."""
        self._head = None
        self._size = 0


    def __len__(self):
        """Return the number of elements in the linkedlist."""
        return self._size

    def is_empty(self):
        """Return True if the linkedlist is empty."""
        return self._size == 0

    def top(self):
        """Return (but do not remove) the element at the top of the linkedlist.

        Raise Empty exception if the linkedlist is empty.
        """
        if self.is_empty():
            raise Empty('list is empty')
        return self._head._element              # head of list


    def insert_from_head(self, e):
        """Add element e to the head of the linkedlist."""
        # Create a new link node and link it
        new_node = self._Node(e, self._head)
        self._head = new_node
        self._size += 1



    def delete_from_head(self):
        """Remove and return the element from the head of the linkedlist.

        Raise Empty exception if the linkedlist is empty.
        """
        if self.is_empty():
            raise Empty('list is empty')
        to_return = self._head._element
        self._head = self._head._next
        self._size -= 1
        return to_return

    def __str__(self):
        result = []
        result.append("head --> ")
        curNode = self._head
        while (curNode is not None):
            result.append(str(curNode._element) + " --> ")
            curNode = curNode._next
        result.append("None")
        return "".join(result)

    def sameSame(self, otherlist):
        # Checks whether two lists contain the same elements in the same order
        # returns True if same, return False otherwise.
        # @parameter1: otherlist, the list comparing with self list.
        # @return: True or False

        # To do
        if self.is_empty():
            raise Empty('list is empty')
        if self._size != otherlist._size:
            return False
        
        curNode = self._head
        other = otherlist._head
        while curNode is not None:
            if curNode._element != other._element:
                return False
            
            curNode = curNode._next
            other = other._next
        return True
                
            
        

    def remove_all_occurance(self, value):
        # remove all occurance of value in linked list. return nothing.
        # Example:
        # head --> 5 --> 4 --> 2 --> 4 --> 1 --> 9 --> 4 --> None
        # >>> l.remove_all_occurance(4)
        # head --> 5 --> 2 --> 1 --> 9 --> None
        # @parameter1: value, the value we are trying to remove from the self list.
        # @return: Nothing

        # To do
    
        if self.is_empty():
            raise Empty('list is empty')
    
        while self._head is not None and self._head._element == value: 
            self._head = self._head._next
    
        if self._head is not None: 
            current = self._head
            while current._next is not None: 
                if current._next._element == value: 
                    current._next = current._next._next 
                else:
                    current = current._next
                


            
            
    def reverse(self):
        
        # reverses self list.
        # Example:
        # head --> 1 --> 2 --> 3 --> 4 --> None
        # >>> l.reverse()
        # head --> 4 --> 3 --> 2 --> 1 --> None
        # @return: Nothing
		
        # To do
        if self.is_empty():
            raise Empty('list is empty')
        prev = None
        currNode = self._head
        nex = currNode._next
          
        while currNode is not None:        
            currNode._next = prev       
            prev = currNode
            currNode = nex
            if nex is not None:
                nex = nex._next       
        self._head = prev



# Flip those booleans to enable test cases
sameSameTest = True
remove_all_occuranceTest = True
reverseTest = True


if (sameSameTest):
    print("-----------Testing sameSame-------------")
    l1 = SingleLinkedList()
    l2 = SingleLinkedList()
    for i in range(5):
        l1.insert_from_head(i)
        l2.insert_from_head(i)
    print("Is l1 sameSame l2? Your answer:", l1.sameSame(l2))   # True

if (remove_all_occuranceTest):
    print("-----------Testing remove_all_occurance-------------")
    l1 = SingleLinkedList()
    for i in range(10):
        l1.insert_from_head(6)
    print(l1)  # 6-->6-->6-->6-->6-->6-->6-->6-->6-->6-->None
    l1.remove_all_occurance(6)
    print(l1)  # None

if (reverseTest):
    print("-----------Testing reverse-------------")
    l1 = SingleLinkedList()
    for i in range(10):
        l1.insert_from_head(i)
    print(l1)  # 9-->8-->7-->6-->5-->4-->3-->2-->1-->0-->None
    l1.reverse()
    print(l1)  # 0-->1-->2-->3-->4-->5-->6-->7-->8-->9-->None