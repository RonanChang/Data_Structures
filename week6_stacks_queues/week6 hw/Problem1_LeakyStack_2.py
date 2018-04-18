class LeakyStack():
    def __init__(self, max_size):
        self._data = [None] * max_size
        self._size = 0    # Track current number of elements
        self._top = 0  # Use this variable to make the stack circular


    def push(self, e):  # O(1)
        max_size = len(self._data)
        if self._size < max_size - 1:
            self._size += 1
        self._data[self._top] = e
        
        self._top += 1
        self._top %= self._size + 1
        
#        print("Test", self._data)
            

    def pop(self):      # O(1)
        ret = self._data[1-self._top]
        self._data[1-self._top] = None
        self._top += 1
        self._top %= self._size
        self._size -= 1
        return ret

    def __len__(self):  # O(1)
        return self._size

    def is_empty(self): # O(1)
        return self._size == 0
        

    def __str__(self):  # O(n) or O(1) up to you
        dat = self._data[self._top:] + self._data[:self._top]
        return str(dat[::-1])
        

##############TEST CODES#################
leakystack = LeakyStack(5)
leakystack.push('a')
leakystack.push('b')
leakystack.push('c')
leakystack.push('a')
leakystack.push('b')
leakystack.push('c')
print(leakystack)   # c b a
leakystack.push('d')
leakystack.push('e')
print(leakystack)  # e d c b a 
leakystack.push('f')
print(leakystack)   # f e d c b,   a is gone because it is the oldest.
print(leakystack.pop())  # f popped
print(leakystack.pop())  # e popped
print(leakystack.pop())  # f popped
print(leakystack.pop())  # e popped
leakystack.push('c')
leakystack.push('a')
leakystack.push('b')
print(leakystack)