class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class SLL:
  def __init__(self, head=None):
    self.head = head
    self.tail = head
    self.size = 1 if head else 0

  def __len__(self):
    return self.size
 
  def is_empty(self):
    return self.head == None

  def clear(self):
    self.head = self.tail = None
    self.size = 0
    
  def __iter__(self):
    current = self.head
    while current:
      yield current.data
      current = current.next
  
  def __str__(self):
    if self.is_empty():
      return "List is empty"
    result = "=== LIST ITEMS ===\n"
    for node_data in self:
      result += f"{node_data} --> "
    result += "None"
    return result 
  
  def insert_at_start(self, item):
    node = Node(item, self.head)
    if self.is_empty():
      self.tail = node
    self.head = node
    self.size += 1
  
  def insert_at_last(self, item):
    node = Node(item)
    if self.is_empty():
      self.head = self.tail = node
    else:
      self.tail.next = node
      self.tail = node
    self.size += 1
  
  def search(self, item):
    current = self.head
    while current:
      if current.data == item:
        return current 
      current = current.next
    return None
  
  def insert_after(self, address, item):
    if address:
      if address == self.tail:
        self.insert_at_last(item)
      else:
        node = Node(item, address.next)
        address.next = node
        self.size += 1
  
  def delete_first(self):
    if not self.is_empty():
      del_node = self.head.data
      if not self.head.next:
        self.head = self.tail = None
      else:
        self.head = self.head.next
      self.size -= 1
      return del_node
  
  def delete_last(self):
    if not self.is_empty():
      del_node = self.tail.data
      if not self.head.next:
        self.head = self.tail = None
      else:
        current = self.head
        while current.next.next:
          current = current.next
        current.next = None
        self.tail = current 
      self.size -= 1
      return del_node
  
  def delete_after(self, address):
    if address and address.next:
      deleted_node = address.next
      address.next = address.next.next
      if deleted_node == self.tail:
        self.tail = address
      self.size -= 1
      return deleted_node.data

  def get_index(self, item):
    if not self.is_empty():
      current = self.head
      index = 0
      while current:
        if current.data == item:
          return index
        current = current.next
        index += 1

  def get_item_at_index(self, index):
    if (self.is_empty() or (index < 0) or (index >= len(self))):
      raise IndentationError("list index out of range")
    temp = 0
    current = self.head
    while current:
      if temp == index:
        return current 
      current = current.next
      temp += 1

  def insert_at_index(self, index, item):
    if index < 0:
      raise IndexError("list index out of range")
    elif index == 0:
      self.insert_at_start(item)
    elif index >= len(self):
      self.insert_at_last(item)
    else:
      prev = self.get_item_at_index(index-1)
      node = Node(item, prev.next)
      prev.next = node
      self.size += 1

  def delete_at_index(self, index):
    if (self.is_empty() or (index < 0) or (index >= len(self))):
      raise IndexError("list index out of range")
    elif index == 0:
      return self.delete_first()
    elif index == len(self)-1:
      return self.delete_last()
    else:
      prev = self.get_item_at_index(index-1)
      del_node = prev.next.data
      prev.next = prev.next.next
      self.size -= 1
      return del_node

  def reverse_list(self):
    if not self.is_empty():
      if not self.head.next:
        return self.head
      prev = None
      current = self.head
      next = None
      while current:
        next = current.next
        current.next = prev
        prev = current 
        current = next
      self.tail = self.head
      self.head = prev

  def check_and_fix_cycle(self):
    slow = self.head
    fast = self.head
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
      if slow == fast:
        slow = self.head
        if slow == fast:
          while fast.next != slow:
            fast = fast.next
        else:
          while slow.next != fast.next:
            slow = slow.next
            fast = fast.next
        fast.next = None
        self.tail = fast
        current = self.head
        self.size = 0
        while current:
          self.size += 1
          current = current.next
        return True
    return False

  def find_middle(self):
    slow = self.head
    fast = self.head
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
    return slow

  def delete_middle(self):
    if self.is_empty():
      return 
    if self.head.next is None:
      return self.delete_first()
    prev = None
    slow = self.head
    fast = self.head
    while fast and fast.next:
      prev = slow
      slow = slow.next
      fast = fast.next.next
    if slow == self.tail:
      self.tail = prev
    prev.next = slow.next
    self.size -= 1
    return slow.data

    
class sllIterator:
  def __init__(self, start):
    self.current = start
  def __iter__(self):
    return self
  def __next__(self):
    if not self.current:
      raise StopIteration 
    data = self.current.data
    self.current = self.current.next
    return data
      
