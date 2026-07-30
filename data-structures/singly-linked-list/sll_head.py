class Node:
  def __init__(self, data, next = None):
    self.data = data
    self.next = next

class SLL:
  def __init__(self, head = None):
    self.head = head
    self.size = 0
    current = self.head
    while current:
      self.size += 1
      current = current.next
  
  def __len__(self):
    return self.size
  
  def __iter__(self):
    current = self.head
    while current:
      yield current.data 
      current = current.next
    
  def __str__(self):
    if self.is_empty():
      return "List is empty"
    self.check_and_fix_cycle()
    result = []
    for node_data in self:
      result.append(f"{node_data}")
    return " --> ".join(result) + " --> None"
  
  def is_empty(self):
    return self.head == None 
  
  def search(self, item):
    current = self.head
    while current:
      if current.data == item:
        return current 
      current = current.next
    return 
  
  def find_index(self, item):
    index = 0
    current = self.head
    while current:
      if current.data == item:
        return index
      index += 1
      current = current.next
    return -1
  
  def find_middle(self):
    slow = self.head
    fast = self.head
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
    return slow
  
  def has_cycle(self):
    slow = self.head
    fast = self.head
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
      if slow == fast:
        return True
    return False
  
  def get_at_index(self, index):
    if (self.is_empty() or (index < 0) or (index >= len(self))):
      raise IndexError("Out of range")
    temp = 0
    current = self.head
    while current:
      if temp == index:
        return current
      temp += 1
      current = current.next
  
  def insert_at_index(self, index, item):
    if index < 0:
      raise IndexError("Index cannot be negative")
    if index == 0:
      self.insert_at_start(item)
      return 
    if index >= len(self):
      self.insert_at_last(item)
      return 
    prev = self.get_at_index(index - 1)
    node = Node(item, prev.next)
    prev.next = node
    self.size += 1
    
  def insert_at_start(self, item):
    node = Node(item, self.head)
    self.head = node
    self.size += 1
  
  def insert_at_last(self, item):
    node = Node(item)
    if self.is_empty():
      self.head = node
      self.size += 1
      return 
    current = self.head
    while current.next:
      current = current.next
    current.next = node
    self.size += 1
  
  def insert_after(self, address, item):
    if address:
      node = Node(item, address.next)
      address.next = node
      self.size += 1
  
  def remove_at_start(self):
    if self.is_empty():
      return 
    del_node = self.head.data
    self.head = self.head.next
    self.size -= 1
    return del_node
    
  def remove_at_last(self):
    if self.is_empty():
      return 
    del_node = None
    if not self.head.next:
      del_node = self.head.data
      self.head = None
    else:
      current = self.head
      while current.next.next:
        current = current.next
      del_node = current.next.data
      current.next = None
    self.size -= 1
    return del_node
  
  def remove_item(self, item):
    if self.is_empty():
      return 
    del_node = None
    if self.head.data == item:
      del_node = self.head.data
      self.head = self.head.next
      self.size -= 1
    else: 
      current = self.head
      while current.next:
        if current.next.data == item:
          del_node = current.next.data
          current.next = current.next.next
          self.size -= 1
          break
        current = current.next    
    return del_node      #stop
  
  def clear(self):
    self.head = None
    self.size = 0
  
  def remove_at_index(self, index):
    if ((index < 0) or (index >= len(self))):
      raise IndexError("Index out of range")
    if index == 0:
      return self.remove_at_start()
    prev = self.get_at_index(index-1)
    del_node = prev.next.data
    prev.next = prev.next.next
    self.size -= 1
    return del_node
  
  def delete_duplicates(self):
    if self.is_empty():
      return 
    current = self.head
    seen = set([current.data])
    while current.next:
      if current.next.data in seen:
        current.next = current.next.next
        self.size -= 1
      else:
        seen.add(current.next.data)
        current = current.next
  
  def deleteEntaireInstanceOfItem(self, item):
    if self.is_empty():
      return
    while self.head and self.head.data == item:
      self.head = self.head.next
      self.size -= 1
    current = self.head
    while current and current.next:
      if current.next.data == item:
        current.next = current.next.next
        self.size -= 1
      else:
        current = current.next
  
  def delete_middle(self):
    if self.is_empty():
      return 
    del_node = None
    if not self.head.next:
      del_node = self.head.data
      self.head = None
    else:
      prev = None
      slow = self.head
      fast = self.head 
      while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
      del_node = slow.data
      prev.next = slow.next
    self.size -= 1
    return del_node
  
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
        self.size = 0
        current = self.head
        while current:
          self.size += 1
          current = current.next
        return True
    return False
    
  def reverse_list(self):
    if self.is_empty():
      return 
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
    self.head = prev
    return prev
