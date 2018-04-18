class LeakyStack():
    def __init__(self, max_size):
        self.array = [None] * max_size
        self.current_size = 0    # Track current number of elements
        self.top = 0  # Use this variable to make the stack circular


    def push(self, e):  # O(1)
        self.array[self.top] = e
        self.top = (self.top + 1) % len(self.array)
        self.current_size += 1
        self.current_size = min(self.current_size, len(self.array))

    def pop(self):      # O(1)
        if not (self.is_empty()):
            self.top = (self.top - 1) % len(self.array)
            top = self.array[self.top]
            self.current_size -= 1
            return top

    def __len__(self):  # O(1)
        return self.current_size

    def is_empty(self): # O(1)
        return self.current_size == 0

    def __str__(self):  # O(n)
        result = []
        for i in range(self.current_size):
            result.append(str(self.array[self.top - i - 1]) + " ")
        return "".join(result)

##############TEST CODES#################
leakystack = LeakyStack(5)
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
