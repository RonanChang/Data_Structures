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
    


def reverseListUsingStack(list1):
    # to do
    s = ArrayStack()    
    s.array = list1
    new_list = ArrayStack()
    while not s.is_empty():
        new_list.push(s.pop())
    return new_list.array


#test:
print(reverseListUsingStack([1,2,3,4]))
 



    
