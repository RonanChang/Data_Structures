class Empty:
    pass

class ArrayStack:
  def __init__(self):
    self.array = []

  def __len__(self):
    return len(self.array)

  def is_empty(self):
    return len(self.array) == 0

  def push(self, e):
    self.array.append(e)

  def top(self):
    if self.is_empty():
      raise Empty()
    return self.array[-1]

  def pop(self):
    if self.is_empty():
      raise Empty()
    return self.array.pop(-1)

  def __repr__(self):
      return str(self.array)
    
def spans1(X):
    result = []
    for i in range(len(X)):
        spans = 1
        while (spans <= i) and (X[i - spans] <= X[i]):
            spans += 1
        result.append(spans)
    return result


print(spans1([6,3,4,5,2])) # [1, 1, 2, 3, 1]
print(spans1([6,7,1,3,4,5,2]))  # [1, 2, 1, 2, 3, 4, 1]

def spans2(X):
    stack = ArrayStack()
    result = []
    for i in range(len(X)):
        while (not stack.is_empty()) and (X[stack.top()] <= X[i]):
            stack.pop()
        
        if stack.is_empty():
            result.append(i + 1)

        else:
            result.append(i - stack.top())
        stack.push(i)
    return result

print(spans2([6,3,4,5,2])) # [1, 1, 2, 3, 1]
print(spans2([6,7,1,3,4,5,2]))  # [1, 2, 1, 2, 3, 4, 1]
    
