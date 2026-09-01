class QueueUnderflowError(IndexError):
  pass

class QueueOverflowError(OverflowError):
  pass

class Queue:
  def __init__(self, capacity=None):
    self.__items = []
    self.__capacity = capacity

  def __str__(self):
    if self.is_empty():
      return "Queue is empty"
    result = [str(item) for item in self]
    return f"=== QUEUE ITEMS ===\n[FRONT] {' -> '.join(result)} [REAR]"

  def __iter__(self):
    return iter(self.__items)

  def __len__(self):
    return len(self.__items)

  def __repr__(self):
    return f"Queue(size={len(self)})"

  def is_empty(self):
    return len(self) == 0

  def is_full(self):
    if self.__capacity is None:
      return False
    return len(self) >= self.__capacity
  
  def enqueue(self, data):
    if self.is_full():
      raise QueueOverflowError("Cannot enqueue; 'Queue' is full")
    self.__items.append(data)

  def dequeue(self):
    if self.is_empty():
      raise QueueUnderflowError("Cannot dequeue; 'Queue' is empty.")
    return self.__items.pop(0)

  def get_rear(self):
    if self.is_empty():
      raise QueueUnderflowError("Cannot peek rear; 'Queue' is empty.")
    return self.__items[-1]

  def get_front(self):
    if self.is_empty():
      raise QueueUnderflowError("Cannot peek front; 'Queue' is empty.")
    return self.__items[0]

  def clear(self):
    self.__items.clear()
