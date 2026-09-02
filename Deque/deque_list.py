class DequeUnderflowError(IndexError):
  pass
class DequeOverflowError(OverflowError):
  pass
  
class Deque:
  def __init__(self, capacity=None):
    self.__items = []
    self.capacity = capacity

  def __iter__(self):
    return iter(self.__items)

  def __str__(self):
    if self.is_empty():
      return "List is empty"
    deque_items = [str(item) for item in self]
    return f"=== DEQUE ITEMS ===\n[FRONT] {' -> '.join(deque_items)} [REAR]"

  def __repr__(self):
    return f'Deque(size={len(self)})'

  def __len__(self):
    return len(self.__items)

  def is_empty(self):
    return len(self.__items) == 0

  def is_full(self):
    if self.capacity is None:
      return False
    return len(self.__items) >= self.capacity

  def insert_at_front(self, data):
    if self.is_full():
      raise DequeOverflowError("Cannot insert an item; 'Deque' is full")
    self.__items.insert(0, data)

  def insert_at_rear(self, data):
    if self.is_full():
      raise DequeOverflowError("Cannot insert an item; 'Deque' is full")
    self.__items.append(data)

  def delete_front(self):
    if self.is_empty():
      raise DequeUnderflowError("Cannot delete front; 'Deque' is empty")
    return self.__items.pop(0)

  def delete_rear(self):
    if self.is_empty():
      raise DequeUnderflowError("Cannot delete rear; 'Deque' is empty")
    return self.__items.pop()

  def get_front(self):
    if self.is_empty():
      raise DequeUnderflowError("Cannot peek front; 'Deque' is empty")
    return self.__items[0]

  def get_rear(self):
    if self.is_empty():
      raise DequeUnderflowError("Cannot peek rear; 'Deque' is empty")
    return self.__items[-1]

  def clear(self):
    self.__items.clear()
