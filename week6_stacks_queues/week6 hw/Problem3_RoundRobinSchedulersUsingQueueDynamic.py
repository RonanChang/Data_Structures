from queue import Empty

class ArrayQueue:
  """FIFO queue implementation using a Python list as underlying storage."""
  DEFAULT_CAPACITY = 5          # moderate capacity for all new queues

  def __init__(self):
    """Create an empty queue."""
    self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
    self._size = 0
    self._front = 0

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
    if self.is_empty():
      raise Empty('Queue is empty')
    return self._data[self._front]

  def dequeue(self):
    """Remove and return the first element of the queue (i.e., FIFO).

    Raise Empty exception if the queue is empty.
    """
    if self.is_empty():
      raise Empty('Queue is empty')
    answer = self._data[self._front]
    self._data[self._front] = None         # help garbage collection
    self._front = (self._front + 1) % len(self._data)
    self._size -= 1
    if 0<self._size<len(self._data)//4:
        self._resize(len(self._data)//2)
    return answer

  def enqueue(self, e):
    """Add an element to the back of queue."""
    if self._size == len(self._data):
      self._resize(2 * len(self.data))     # double the array size
    avail = (self._front + self._size) % len(self._data)
    self._data[avail] = e
    self._size += 1

  def _resize(self, cap):                  # we assume cap >= len(self)
    """Resize to a new list of capacity >= len(self)."""
    old = self._data                       # keep track of existing list
    self._data = [None] * cap              # allocate list with new capacity
    walk = self._front
    for k in range(self._size):            # only consider existing elements
      self._data[k] = old[walk]            # intentionally shift indices
      walk = (1 + walk) % len(old)         # use old size as modulus
    self._front = 0                        # front has been realigned
 
  def __repr__(self):                       # print the contents of Queue
    return str(self._data)

  def rotate(self):
    # to do
    # don't Q.enqueue(Q.dequeue( ))
    # just swap
     
    self._data[self._front],self._data[(self._front + self._size)%len(self._data)] = self._data[(self._front+ self._size)%len(self._data)],self._data[self._front]
    self._front = (self._front + 1)%len(self._data)

    
    


queue1 = ArrayQueue()
queue1.enqueue(3)
queue1.enqueue(5)
queue1.enqueue(7)
queue1.enqueue(9)
print("1. Length of Queue: ",len(queue1))
print("1. Current Contents of Queue: ",queue1) #Output: 1. Current Contents of Queue:  [3, 5, 7, 9, None]
print("\n")

print("Dequeued Element: ",queue1.dequeue())
print("2. Length of Queue",len(queue1))
print("2. Current Contents of Queue: ",queue1) #Output: 2. Current Contents of Queue:  [None, 5, 7, 9, None]
print("\n")



queue1.rotate()
print("3. Length of Queue: ",len(queue1))
print("3. After Rotating, Current Contents of Queue: ",queue1) #Output: 3. After Rotating, Current Contents of Queue:  [None, None, 7, 9, 5]
print("\n")


queue1.rotate()
print("4. Length of Queue: ",len(queue1))
print("4. After Rotating, Current Contents of Queue: ",queue1) #Output: 4. After Rotating, Current Contents of Queue:  [7, None, None, 9, 5]


