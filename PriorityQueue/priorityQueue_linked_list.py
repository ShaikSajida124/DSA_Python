class PriorityQueueUnderflowError(IndexError): pass
class PriorityQueueOverflowError(OverflowError): pass
  
class Node:
  def __init__(self, data, priority, next=None):
    self.data = data
    self.priority = priority
    self.next = next

class PriorityQueue:
  def __init__(self, capacity=None):
    self.head = None
    self.capacity = capacity
    self.size = 0

  def __repr__(self):
    return f"PriorityQueue(size={len(self)})"

  def __len__(self):
    return self.size

  def __str__(self):
    if self.is_empty():
      return "Priority Queue is empty"
    result = [str(node) for node in self]
    return f"=== PRIORITY QUEUE ITEMS===\n{' -> '.join(result)}"

  def __iter__(self):
    current = self.head
    while current:
      yield (current.data, current.priority)
      current = current.next

  def is_empty(self):
    return self.head is None

  def is_full(self):
    if self.capacity is None:
      return False
    return len(self) >= self.capacity

  def push(self, item, priority):
    if self.is_full():
      raise PriorityQueueOverflowError("Cannot insert an item; 'PriorityQueue' is full")
    node = Node(item, priority)
    if self.is_empty() or self.head.priority > priority:
      node.next = self.head
      self.head = node
    else:
      current = self.head
      while current.next and current.next.priority <= priority:
        current = current.next
      node.next = current.next
      current.next = node
    self.size += 1

  def pop(self):
    if self.is_empty():
      raise PriorityQueueUnderflowError("Cannot delete an item; 'PriorityQueue' is empty")
    del_node_data = self.head.data
    self.head = self.head.next
    self.size -= 1
    return del_node_data

  def clear(self):
    self.head = None
    self.size = 0

  

  
