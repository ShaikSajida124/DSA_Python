class EmptyStackError(IndexError):
  pass
class FullStackError(OverflowError):
  pass
class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class Stack:
  def __init__(self, capacity=None):
    self.start = None
    self.capacity = capacity
    self._size = 0

  def __len__(self):
    return self.size

  def is_empty(self):
    return self.start is None

  def is_full(self):
    if self.capacity is None:
      return False
    return len(self) >= self.capacity

  def push(self, item):
    if self.is_full():
      raise FullStackError("'Stack' is full; cannot push an item")
    node = Node(item, self.start)
    self.start = node
    self._size += 1

  def pop(self):
    if self.is_empty():
      raise EmptyStackError("'Stack' is empty; cannot pop an item")
    deleted_item = self.start.data
    self.start = self.start.next
    self._size -= 1
    return deleted_item

  def peek(self):
    if self.is_empty():
      raise EmptyStackError("'Stack' is empty")
    return self.start.data

  
    
