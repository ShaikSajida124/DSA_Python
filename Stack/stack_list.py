class EmptyStackError(IndexError):
  pass
  
class FullStackError(OverflowError):
  pass
  
class Stack:
  def __init__(self):
    self.__items = []
    self.__capacity = None #YOU CAN SET CAPACITY 

  def __str__(self):
    if self.is_empty():
      return 'Stack is empty'
    result = [str(item) for item in self.__items]
    result.reverse()
    return f"=== STACK ITEMS ===\nTop -> {' -> '.join(result)} -> None"

  def __iter__(self):
    return reversed(self.__items)

  def __len__(self):
    return len(self.__items)

  def __repr__(self):
    return f'Stack(size={len(self.__items)})'

  def clear(self):
    return self.__items.clear()
  
  def is_empty(self):
    return len(self.__items) == 0

  def is_full(self):
    if self.__capacity is None:
      return False
    return len(self.__items) >= self.__capacity

  def push(self, data):
    if self.is_full():
      raise FullStackError("'Stack' is Full")
    self.__items.append(data)

  def pop(self):
    if self.is_empty():
      raise EmptyStackError("'Stack' is empty, cannot pop an element")
    return self.__items.pop()

  def peek(self):
    if self.is_empty():
      raise EmptyStackError("'Stack' is empty")
    return self.__items[-1]
