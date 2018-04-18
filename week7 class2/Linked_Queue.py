class Empty(BaseException):
    def __init__(self, message):
      self.message = message

class LinkedQueue:
  """FIFO queue implementation using a singly linked list for storage."""

  #-------------------------- nested _Node class --------------------------
  class _Node:
    """Lightweight, nonpublic class for storing a singly linked node."""
    __slots__ = '_element', '_next'         # streamline memory usage

    def __init__(self, element, next):
      self._element = element
      self._next = next

  #------------------------------- queue methods -------------------------------
  def __init__(self):
    """Create an empty queue."""
    self._head = None
    self._tail = None
    self._size = 0                          # number of queue elements

  def __len__(self):
    """Return the number of elements in the queue."""
    return self._size

  def is_empty(self):
    """Return True if the queue is empty."""
    return self._size == 0

  def first(self):
    """Return (but do not remove) the element at the front of the queue.

    Raise Empty exception if the queue is empty.
    """
    # TO DO
    if self.is_empty():
        raise Empty("Empty!")
    return self._head._element

  def dequeue(self):
    """Remove and return the first element of the queue (i.e., FIFO).

    Raise Empty exception if the queue is empty.
    """
    # TO DO
    
    self._head = self._head._next
    self._prev = None
    self._size -= 1

  def enqueue(self, e):
    """Add an element to the back of queue."""
    # TO DO
    newest = self._Node(e,None)
    if self.is_empty():
        self._head = newest
    else:
        self._tail._next = newest
    self._tail = newest
    self._size += 1

  def __str__(self):
    # TO DO
    result = []
    curNode = self._head
    while (curNode is not None):
      result.append(str(curNode._element) + " --> ")
      curNode = curNode._next
    result.append("None")
    return "".join(result)


queue = LinkedQueue()
queue.enqueue("First")
queue.enqueue("Second")
queue.enqueue("Third")
queue.enqueue("Fourth")

print(queue)        # Head --> First Second Third Fourth <-- Tail
print("Dequeue: ", queue.dequeue())  # Should pop First
print(queue)         # Head --> Second Third Fourth <-- Tail
