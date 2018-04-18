class SharedMemoryStack():

    DEFAULT_CAPACITY = 10
    def __init__(self):
        self._data = [None] * SharedMemoryStack.DEFAULT_CAPACITY
        self.stack1_size = 0
        self.stack2_size = 0

    def pushStack1(self, e):
        self._data[self.stack1_size] = e
        self.stack1_size += 1

    def pushStack2(self, e):
        self._data[-(self.stack2_size + 1)] = e
        self.stack2_size += 1

    def popStack1(self):
        self._data[self.stack1_size-1] = None
        self.stack1_size -= 1
        return self.peekStack1()

    def popStack2(self):
        self._data[-self.stack2_size] = None
        self.stack2_size -= 1
        return self.peekStack2()

    def is_full(self):
        return self.stack1_size + self.stack2_size == SharedMemoryStack.DEFAULT_CAPACITY

    def is_empty1(self):
        return self.stack1_size == 0

    def is_empty2(self):
        return self.stack2_size == 0

    def peekStack1(self):
        return self._data[:self.stack1_size]

    def peekStack2(self):
        return self._data[-1:-self.stack2_size-1:-1]

    def __str__(self):
        result = []
        result.append("Stack 1: ")
        # Your code 1 to show stack 1
        
        for each in self.peekStack1():
            result.append(str(each))
            result.append(", ")
                 
        result.append("STack 2: ")
        # Your code 2 to show stack 2
        for each in self.peekStack2():
            result.append(str(each))
            result.append(", ")

        return "".join(result)


stack = SharedMemoryStack()
stack.pushStack1(1)
stack.pushStack1(2)
stack.pushStack1(3)
stack.pushStack1(4)
stack.pushStack2(5)
stack.pushStack2(6)
stack.pushStack2(7)
stack.pushStack2(8)
stack.pushStack2(9)
stack.pushStack2(10)
print(stack)  # Stack 1: 1, 2, 3, 4; Stack 2: 5, 6, 7, 8, 9, 10
print("Popping: ", stack.popStack1())  # popped 4
print("Popping: ", stack.popStack2())
stack.pushStack2(11) # Stack 1: 1, 2, 3; Stack 2: 5, 6, 7, 8, 9, 10, 11
print(stack)

