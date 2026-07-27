class Node:
  def __init__(self, data, prev=None, next=None):
    self.data = data
    self.prev = prev
    self.next = next

class CDLL:
  def __init__(self, head=None):
    self.head = head
    self.size = 0

  def __len__(self):
    return self.size

  def __str__(self):
    if self.is_empty():
      return "List is empty"
    result = []
    current = self.head
    for node in range(len(self)):
      result.append(str(current.data))
      current = current.next
    result.append("(Head)")
    return " <--> ".join(result)

  def __iter__(self):
    return CDLLIterator(self.head)

  def is_empty(self):
    return self.head == None

  def clear(self):
    self.head = None
    self.size = 0

  def insert_at_start(self, item):
    self.insert_at_last(item)
    self.head = self.head.prev

  def insert_at_last(self, item):
    node = Node(item)
    if self.is_empty():
      node.prev = node.next = node
      self.head = node
    else:
      node.prev = self.head.prev
      node.next = self.head
      self.head.prev.next = node
      self.head.prev = node
    self.size += 1

  def search(self, item):
    if self.is_empty():
      return None
    current = self.head
    while True:
      if current.data == item:
        return current 
      current = current.next
      if current == self.head:
        break
    return None

  def insert_after(self, address, item):
    if address:
      node = Node(item, address, address.next)
      address.next.prev = node
      address.next = node
      self.size += 1

  def delete_start(self):
    if self.is_empty():
      return 
    if self.head.next == self.head:
      self.head = None
    else:
      self.head.prev.next = self.head.next
      self.head.next.prev = self.head.prev
      self.head = self.head.next
    self.size -= 1

  def delete_last(self):
    if self.is_empty():
      return 
    if self.head.next == self.head:
      self.head = None
    else:
      self.head.prev.prev.next = self.head
      self.head.prev = self.head.prev.prev
    self.size -= 1

  def delete_item(self, item):
    address = self.search(item)
    if address:
      if address == self.head or address.next == address:
        self.delete_start()
      else:
        address.prev.next = address.next
        address.next.prev = address.prev
        self.size -= 1

  def find_index(self, item):
    for index, data in enumerate(self):
      if data == item:
        return index
    return -1

  def get_item_at_index(self, index):
    if (self.is_empty() or (index < 0) or (index >= len(self))):
      raise IndexError("list index out of range")
    current = self.head
    for node in range(index):
      current = current.next
    return current 
    
  def insert_at_index(self, index, item):
    if index < 0:
      raise IndexError("list index out of range")
    elif index == 0 or self.is_empty():
      self.insert_at_start(item)
    elif index >= len(self):
      self.insert_at_last(item)
    else:
      position = self.get_item_at_index(index)
      node = Node(item, position.prev, position)
      position.prev.next = node
      position.prev = node
      self.size += 1

  def delete_at_index(self, index):
    if (self.is_empty() or (index < 0) or (index >= len(self))):
      raise IndexError("list index out of range")
    elif index == 0:
      self.delete_start()
    else:
      position = self.get_item_at_index(index)
      position.prev.next = position.next
      position.next.prev = position.prev
      self.size -= 1
    
  def find_middle(self):
    if self.is_empty():
      return 
    if self.head.next == self.head:
      return self.head
    else:
      slow = self.head
      fast = self.head
      while True:
        slow = slow.next
        fast = fast.next.next
        if fast == self.head or fast.next == self.head:
          return slow

  def delete_middle(self):
    if self.is_empty():
      return 
    if self.head.next == self.head:
      self.head = None
    else:
      mid_node = self.find_middle()
      mid_node.prev.next = mid_node.next
      mid_node.next.prev = mid_node.prev
    self.size -= 1

  def reverse_list(self):
    if self.is_empty():
      return 
    if self.head.next == self.head:
      return self.head
    else:
      prev = self.head.prev
      current = self.head
      next = None
      while True:
        next = current.next
        current.next = prev
        current.prev = next
        prev = current
        current = next
        if current == self.head:
          break
      self.head = prev
      return self.head
    

class CDLLIterator:
  def __init__(self, start):
    self.current = start
    self.stop = start
    self.first_pass = True

  def __iter__(self):
    return self

  def __next__(self):
    if not self.current or not self.first_pass:
      raise StopIteration 
    data = self.current.data
    self.current = self.current.next
    if self.current == self.stop:
      self.first_pass = False
    return data
