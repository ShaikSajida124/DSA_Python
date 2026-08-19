from sll_head_tail import*
class QueueUnderFlowError(IndexError):
  pass

class QueueOverFlowError(OverflowError):
  pass

class Queue:
  def __init__(self, capacity=None):
    self.__items = SLL()
    self.__capacity = capacity

  def __len__(self):
    return len(self.__items)

  def __str__(self):
    if self.is_empty():
      return "List is empty"
    result = [str(item) for item in self]
    return f"=== QUEUE ITEMS ===\n[FRONT] {' -> '.join(result)} [REAR]"

  def __iter__(self):
    return iter(self.__items)

  def __repr__(self):
    return f"Queue(size={len(self)})"

  def is_empty(self):
    return self.__items.is_empty()

  def is_full(self):
    if self.__capacity is None:
      return False
    return len(self) >= self.__capacity

  def enqueue(self, data):
    if self.is_full():
      raise QueueOverflowError("Cannot enqueue; 'Queue' is full.")
    self.__items.insert_at_last(data)

  def dequeue(self):
    if self.is_empty():
      raise QueueUnderflowError("Cannot dequeue; 'Queue' is empty.")
    return self.__items.delete_first()

  def get_front(self):
    if self.is_empty():
      raise QueueUnderflowError("Cannot peek front; 'Queue' is empty.")
    return self.__items.head.data

  def get_rear(self):
    if self.is_empty():
      raise QueueUnderflowError("Cannot peek rear; 'Queue' is empty.")
    return self.__items.tail.data

  def clear(self):
    self.__items.clear()
