class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class CLL:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  def __len__(self):
    return self.size

  def __str__(self):
    if self.is_empty():
      return "List is empty"

    result = [str(node_data) for node_data in self]
    return f"=== LIST ITEMS ===\n{' -> '.join(result)} -> (Head)"

  def __iter__(self):
    return CLLIterator(self.head)

  def is_empty(self):
    return self.head is None

  def clear(self):
    self.head = self.tail = None
    self.size = 0

  def insert_at_start(self, item):
    node = Node(item, self.head)
    if self.is_empty():
      node.next = node
      self.tail = node
    else:
      self.tail.next = node
    self.head = node
    self.size += 1

  def insert_at_last(self, item):
    node = Node(item, self.head)
    if self.is_empty():
      node.next = node
      self.head = node
    else:
      self.tail.next = node
    self.tail = node
    self.size += 1

  def delete_first(self):
    if self.is_empty():
      return
    del_node = self.head.data
    if self.head == self.tail:
      self.head = self.tail = None
    else:
      self.tail.next = self.head.next
      self.head = self.head.next
    self.size -= 1
    return del_node

  def delete_last(self):
    if self.is_empty():
      return
    del_node = self.tail.data
    if self.head == self.tail:
      self.head = self.tail = None
    else:
      current = self.head
      while current.next != self.tail:
        current = current.next
      self.tail = current
      current.next = current.next.next
    self.size -= 1
    return del_node

  def delete_item(self, item):
    if self.is_empty():
      return
    if self.head.data == item:
      return self.delete_first()
    else:
      current = self.head.next
      while current and current.next != self.head:
        if current.next.data == item:
          del_node = current.next.data
          if current.next == self.tail:
            self.tail = current
          current.next = current.next.next
          self.size -= 1
          return del_node
        current = current.next
      

  def search(self, item):
    if self.is_empty():
      return
    current = self.head
    while True:
      if current.data == item:
        return current
      current = current.next
      if current == self.head:
        break
    return 

  def insert_after(self, address, item):
    if address:
      if address == self.tail:
        self.insert_at_last(item)
      else:
        node = Node(item, address.next)
        address.next = node
        self.size += 1

  def findMiddle(self):
    if self.is_empty():
      return
    if self.head == self.tail:
      return self.head
    slow = self.head
    fast = self.head
    while True:
      slow = slow.next
      fast = fast.next.next
      if fast == self.head or fast.next == self.head:
        return slow

  def reverse_list(self):
    if self.is_empty():
      return
    if self.head == self.tail:
      return self.head
    old_head = self.head
    prev = self.tail 
    current = self.head
    next_node = None
    while True:
      next_node = current.next
      current.next = prev
      prev = current
      current = next_node
      if current == old_head:
        break
    self.head = prev
    self.tail = old_head
    return self.head


class CLLIterator:
  def __init__(self, start):
    self.current = start
    self.start = start
    self.stop = False

  def __iter__(self):
    return self

  def __next__(self):
    if not self.current or (self.current == self.start and self.stop == True):
      raise StopIteration
    self.stop = True
    data = self.current.data
    self.current = self.current.next
    return data

cll = CLL()
print("is empty", cll.is_empty())
print("=====insertion=====\n")
cll.insert_at_start("A")
cll.insert_at_last("B")
cll.insert_at_last("C")
print("is empty", cll.is_empty())
print("len=", len(cll))
print(cll)
print("=====Delation=====\n")
print("deleted_node=", cll.delete_first())
print("deleted_node=", cll.delete_last())
print("deleted_node=", cll.delete_first())
print("is empty", cll.is_empty())
print("=====find middle node=====\n")
cll.insert_at_start(10)
cll.insert_at_start(5)
cll.insert_at_last(20)
cll.insert_after(cll.search(10), 15)
print(cll)
print("middle node =", cll.findMiddle().data)
print("=====reverse list======\n")
print(cll)
print("After reversing")
cll.reverse_list()
print(cll)

