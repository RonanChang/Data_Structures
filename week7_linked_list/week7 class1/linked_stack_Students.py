# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from exceptions import Empty

class LinkedStack:
  """LIFO Stack implementation using a singly linked list for storage."""

  #-------------------------- nested _Node class --------------------------
  class _Node:
    """Lightweight, nonpublic class for storing a singly linked node."""
    __slots__ = '_element', '_next'         # streamline memory usage

    def __init__(self, element, next):      # initialize node's fields
      self._element = element               # reference to user's element
      self._next = next                     # reference to next node

  #------------------------------- stack methods -------------------------------
  def __init__(self):
    """Create an empty stack."""
    self._head = None                       # reference to the head node
    self._size = 0                          # number of stack elements

  def __len__(self):
    """Return the number of elements in the stack."""
    return self._size

  def is_empty(self):
    """Return True if the stack is empty."""
    return self._size == 0

  def top(self):
    """Return (but do not remove) the element at the top of the stack.

    Raise Empty exception if the stack is empty.
    """
    if self.is_empty():
      raise Empty('Stack is empty')
    return self._head._element              # top of stack is at head of list


  def push(self, e):
    """Add element e to the top of the stack."""
    # Create a new link node and link it
    # to do
    new = LinkedStack._Node(e,next)
    new._next = self._head
    self._head = new
    self._size += 1
    
    return self.printAll()


  def pop(self):
    """Remove and return the element from the top of the stack (i.e., LIFO).

    Raise Empty exception if the stack is empty.
    """
    if self.is_empty():
      raise Empty('Stack is empty')
    # Delete node from Stack
    # to do
    
    self._head = self._head._next
    self._size -= 1
    return self.printAll()

  def unOrderedSearch(self,target):
      # Search for the target element in the Stack
      # to do
      curNode = self._head
      while (curNode is not None) and curNode._element != target:
          curNode = curNode._next
      return (curNode is not None)

  def printAll(self):
      # print the contents of the Stack
      # to do
      output = ""
      curNode = self._head
      while curNode != None:
          output += str(curNode._element)
          output += ","
          curNode = curNode._next
      return output
    
linkedStack1 = LinkedStack()
linkedStack1.push(5)
print(linkedStack1.push(10))
linkedStack1.push(22)
linkedStack1.push(35)

print(linkedStack1.unOrderedSearch(10))
print(linkedStack1.unOrderedSearch(5))
print("Stack contents: "+linkedStack1.printAll())
print(linkedStack1.pop())
print(linkedStack1.pop())
print(linkedStack1.unOrderedSearch(35))
print("Stack contents: "+linkedStack1.printAll())