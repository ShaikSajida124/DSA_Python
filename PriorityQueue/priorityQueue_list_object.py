class PriorityQueueUnderflowError(IndexError): pass

class PriorityQueueOverflowError(OverflowError):
  pass
#priority Queue
class PriorityQueue:
  def __init__(self, capacity=None):
    self.__items = []
    self.capacity = capacity

  def __len__(self):
    return len(self.__items)

  def __str__(self):
    if self.is_empty():
      return "PriorityQueue is empty"
    result = [str(item) for item in self]
    return f"=== PRIORITY QUEUE ITEMS ===\n{' -> '.join(result)}"

  def __repr__(self):
    return f"PriorityQueue(size={len(self)})"

  def is_empty(self):
    return len(self) == 0

  def is_full(self):
    if self.capacity is None:
      return False
    return len(self) >= self.capacity

  def __iter__(self):
    return iter(self.__items)

  def push(self, container):
    if self.is_full():
      raise PriorityQueueOverflowError("Cannot add an item; 'PriorityQueue' is full")
    priority = container[0]
    for i in range(len(self)):
      current_priority = self.__items[i][0]
      if priority < current_priority:
        self.__items.insert(i, container)
        return
    self.__items.append(container)
    
  def pop(self):
    if self.is_empty():
      raise PriorityQueueUnderflowError("Cannot delete an item; 'PriorityQueue' is empty")
    return self.__items.pop(0)

  def clear(self):
    self.__items.clear()
