class Empty(BaseException):
    def __init__(self, message):
      self.message = message

class LinkedDeque:
  """Deque implementation using a doubly linked list for storage."""

  #-------------------------- nested _Node class --------------------------
  class _Node:
    """Lightweight, nonpublic class for storing a doubly linked node."""
    __slots__ = '_element', '_next', '_prev'         # streamline memory usage

    def __init__(self, element, prev, next):
      self._element = element
      self._prev = prev
      self._next = next

      

  #------------------------------- queue methods -------------------------------
  def __init__(self):
    """Create an empty deeue."""
    self._head = None
    self._tail = None
    self._size = 0                          # number of elements

  def __len__(self):
    """Return the number of elements in the queue."""
    return self._size

  def is_empty(self):
    """Return True if the queue is empty."""
    return self._size == 0

  def first(self):
    """Return (but do not remove) the element at the front of the queue.

    Raise Empty exception if the deque is empty.
    """
    if self.is_empty():
      raise Empty('Queue is empty')
    return self._head._element              # front aligned with head of list

  def last(self):
    """Return (but do not remove) the element at the end of the queue.

    Raise Empty exception if the deque is empty.
    """
    # Your code
    if self.is_empty():
        raise Empty("Queue is empty")
    return self._tail._element


  def delete_first(self):
    """Remove and return the first element of the deque.

    Raise Empty exception if the queue is empty.
    """
    if self.is_empty():
      raise Empty('Queue is empty')
    answer = self._head._element
    self._head = self._head._next
    self._size -= 1
    if self.is_empty():                     # special case as deque is empty
      self._tail = None                     # removed head had been the tail
    else:
      self._head._prev = None
    return answer

  def delete_last(self):
    """Remove and return the last element of the deque.

    Raise Empty exception if the queue is empty.
    """
    # Your code
    if self.is_empty():
        raise Empty("Empty")
    answer = self._tail._element
    self._tail = self._tail._prev
    self._size -= 1
    if self.is_empty():
        raise("Empty")
    else:
        self._tail._prev = None
    return answer


  def add_first(self, e):
    """Add an element to the front of deque."""
    # Your code
    new = LinkedDeque._Node(e,None,self._head)
    if self.is_empty():
        self._tail = new
    else:
        self._head._prev = new
    self._head = new
    self._size += 1
    


  def add_last(self, e):
    """Add an element to the back of deque."""
    newest = self._Node(e, self._tail, None)            # node will be new tail node, prev point to old tail
    if self.is_empty():
      self._head = newest                   # special case: previously empty
    else:
      self._tail._next = newest
    self._tail = newest                     # update reference to tail node
    self._size += 1


  def __str__(self):
    result = []
    curNode = self._head
    while (curNode is not None):
      result.append(str(curNode._element) + " <--> ")
      curNode = curNode._next
    return "".join(result)

  def print_reverse_order(self):
    """Prints (or returns) the Deque reversely."""
    # Your code
    curNode = self._tail
    output = ""
    while curNode != None:
        output += str(curNode._element)
        output += " <--> "
        curNode = curNode._prev
    
    return output




deque = LinkedDeque()
for i in range(4):
  deque.add_first(i)
for j in range(4):
  deque.add_last(j + 4)

print(deque) # head -> 3 <--> 2 <--> 1 <--> 0 <--> 4 <--> 5 <--> 6 <--> 7 <- tail
print(deque.print_reverse_order())
print("deleting first: ", deque.delete_first())   # 3
print("deleting last: ", deque.delete_last())     # 7
print(deque) # head -> 2 <--> 1 <--> 0 <--> 4 <--> 5 <--> 6 <- tail
