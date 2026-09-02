class DequeUnderflowError(IndexError):
  pass
class DequeOverflowError(OverflowError):
  pass

class Node:
  def __init__(self, data, prev=None, next=None):
    self.data = data
    self.prev = prev
    self.next = next

  
class Deque:
  def __init__(self, capacity=None):
    self.capacity = capacity
    self.front = None
    self.rear = None
    self.size = 0

  def __len__(self):
    return self.size
  
  def __iter__(self):
    return DequeIterator(self.front)

  def __str__(self):
    if self.is_empty():
      return "Deque is empty"
    deque_items = [str(node_data) for node_data in self]
    return f"=== DEQUE ITEMS ===\n[FRONT] {' -> '.join(deque_items)} [REAR]"

  def __repr__(self):
    return f"Deque(size={len(self)})"

  def is_empty(self):
    return self.front is None

  def is_full(self):
    if self.capacity is None:
      return False
    return len(self) >= self.capacity

  def insert_at_front(self, item):
    if self.is_full():
      raise DequeOverflowError("Cannot insert an item; 'Deque' is full")
    node = Node(item, next=self.front)
    if self.is_empty():
      self.rear = node
    else:
      self.front.prev = node
    self.front = node
    self.size += 1

  def insert_at_rear(self, item):
    if self.is_full():
      raise DequeOverflowError("Cannot insert an item; 'Deque' is full")
    node = Node(item, prev=self.rear)
    if self.is_empty():
      self.front = node
    else:
      self.rear.next = node
    self.rear = node
    self.size += 1

  def delete_front(self):
    if self.is_empty():
      raise DequeUnderflowError("Cannot delete an item; 'Deque' is empty")
    del_node_data = self.front.data
    if self.front == self.rear:
      self.front = self.rear = None
    else:
      self.front = self.front.next
      self.front.prev = None
    self.size -= 1
    return del_node_data

  def delete_rear(self):
    if self.is_empty():
      raise DequeUnderflowError("Cannot delete an item; 'Deque' is empty")
    del_node_data = self.rear.data
    if self.front == self.rear:
      self.front = self.rear = None
    else:
      self.rear.prev.next = None
      self.rear = self.rear.prev
    self.size -= 1
    return del_node_data

  def get_front(self):
    if self.is_empty():
      raise DequeUnderflowError("Cannot peek front; 'Deque' is empty")
    return self.front.data

  def get_rear(self):
    if self.is_empty():
      raise DequeUnderflowError("Cannot peek rear; 'Deque' is empty")
    return self.rear.data

  def clear(self):
    self.front = self.rear = None
    self.size = 0
    
#Iterator class
class DequeIterator:
  def __init__(self, start):
    self.current = start

  def __iter__(self):
    return self

  def __next__(self):
    if self.current is None:
      raise StopIteration
    data = self.current.data
    self.current = self.current.next
    return data
