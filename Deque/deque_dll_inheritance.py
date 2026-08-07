#import dll before using the code
import unittest
class DequeUnderFlowError(IndexError):
  pass
class DequeOverFlowError(OverflowError):
  pass

class Deque(DLL):
  def __init__(self, capacity=None):
    self.capacity = capacity
    super().__init__()

  def __str__(self):
    if self.is_empty():
      return "Deque is empty"
    result = [str(item) for item in self]
    return f"=== DEQUE ITEMS ===\n[FRONT] {' -> '.join(result)} [REAR]"

  def __repr__(self):
    return f"Deque(size={len(self)})"

  def is_full(self):
    if self.capacity is None:
      return False
    return len(self) >= self.capacity

  def insert_at_front(self, data):
    if self.is_full():
      raise DequeOverFlowError("Cannot insert an item; 'Deque' is full")
    super().insert_at_start(self, data)

  def insert_at_rear(self, data):
    if self.is_full():
      raise DequeOverFlowError("Cannot insert an item; 'Deque' is full")
    super().insert_at_last(data)

  def delete_front(self):
    if self.is_empty():
      raise DequeUnderFlowError("Cannot delete an item; 'Deque' is empty")
    return super().delete_first()

  def delete_rear(self):
    if self.is_empty():
      raise DequeUnderFlowError("Cannot delete an item; 'Deque' is empty")
    return super().delete_last()

  def get_front(self):
    if self.is_empty():
      raise DequeUnderFlowError("Cannot peek front; 'Deque' is empty")
    return self.head.data

  def get_rear(self):
    if self.is_empty():
      raise DequeUnderFlowError("Cannot peek rear; 'Deque' is empty")
    return self.tail.data

  #Restricted Methods
  def search(self, *args, **kwargs):
    raise AttributeError("'Deque' has no attribute 'search'")

  def find_index(self, *args, **kwargs):
    raise AttributeError("'Deque' has no attribute 'find_index'")

  def find_middle(self):
    raise AttributeError("'Deque' has no attribute 'find_middle'")

  def has_cycle(self):
    raise AttributeError("'Deque' has no attribute 'has_cycle'")

  def get_at_index(self, *args, **kwargs):
    raise AttributeError("'Deque' has no attribute 'get_at_index'")

  def insert_at_index(self, *args, **kwargs):
    raise AttributeError("'Deque' has no attribute 'insert_at_index'")

  def insert_at_start(self, *args, **kwargs):
    raise AttributeError("'Deque' has no attribute 'insert_at_start'")

  def insert_at_last(self, *args, **kwargs):
    raise AttributeError("'Deque' has no attribute 'insert_at_last'")

  def insert_after(self, *args, **kwargs):
    raise AttributeError("'Deque' has no attribute 'insert_after'")

  def delete_first(self):
    raise AttributeError("'Deque' has no attribute 'delete_first'")

  def delete_last(self):
    raise AttributeError("'Deque' has no attribute 'delete_last'")

  def delete_after(self, *args, **kwargs):
    raise AttributeError("'Deque' has no attribute 'delete_after'")

  def delete_item(self, *args, **kwargs):
    raise AttributeError("'Deque' has no attribute 'delete_item'")

  def delete_at_index(self, *args, **kwargs):
    raise AttributeError("'Deque' has no attribute 'delete_at_index'")

  def delete_duplicates(self):
    raise AttributeError("'Deque' has no attribute 'delete_duplicates'")

  def delete_middle(self):
    raise AttributeError("'Deque' has no attribute 'delete_middle'")

  def deleteEntireInstanceOfElement(self, *args, **kwargs):
    raise AttributeError("'Deque' has no attribute 'deleteEntireInstanceOfElement'")

  def print_backward(self):
    raise AttributeError("'Deque' has no attribute 'print_backward'")

  def reverse_list(self):
    raise AttributeError("'Deque' has no attribute 'reverse_list'")
  

  
    

  


class myDeque(unittest.TestCase):
  def test_initialization(self):
    dq = Deque()

    self.assertTrue(dq.is_empty())
    self.assertFalse(dq.is_full())
    self.assertEqual(len(dq), 0)


    dq.insert_at_front(20)
    dq.insert_at_front(10)
    dq.insert_at_rear(30)

    self.assertEqual(dq.get_front(), 10)
    self.assertEqual(dq.get_rear(), 30)
    self.assertEqual(len(dq), 3)
    self.assertFalse(dq.is_empty())

    self.assertEqual(dq.delete_front(), 10)
    self.assertEqual(dq.delete_rear(), 30)
    self.assertEqual(dq.get_front(), 20)
    self.assertEqual(dq.get_rear(), 20)

    
    self.assertEqual(len(dq), 1)

  def test_underflow_exception(self):
    dq = Deque()

    with self.assertRaises(DequeUnderFlowError):
      dq.delete_front()
    with self.assertRaises(DequeUnderFlowError):
      dq.delete_rear()
    with self.assertRaises(DequeUnderFlowError):
      dq.get_front()
    with self.assertRaises(DequeUnderFlowError):
      dq.get_rear()

  def test_overflow_exception(self):
    dq = Deque(3)
    dq.insert_at_front("A")
    dq.insert_at_rear("B")
    dq.insert_at_rear("C")
   
    with self.assertRaises(DequeOverFlowError):
      dq.insert_at_rear("D")
    with self.assertRaises(DequeOverFlowError):
      dq.insert_at_front("F")

  def test_string_outputs(self):
    dq = Deque()
    self.assertEqual(str(dq), "Deque is empty")

    dq.insert_at_front("A")
  dq.insert_at_rear("C")
    output = "=== DEQUE ITEMS ===\n[FRONT] A -> B -> C [REAR]"

    self.assertEqual(str(dq), output)

    dq.clear()
    self.assertTrue(dq.is_empty())
  def test_iteration(self):
    dq = Deque()
    dq.insert_at_front("A")
    dq.insert_at_rear("B")
    dq.insert_at_rear("C")
    myList = []
    for item in dq:
      myList.append(item)
    self.assertEqual(myList, ["A", "B", "C"])

  def test_attributException(self):
    dq = Deque()
    dq.insert_at_front("A")
    dq.insert_at_rear("B")
    dq.insert_at_rear("C")

    with self.assertRaises(AttributeError):
      dq.insert_at_start("c")

    with self.assertRaises(AttributeError):
      dq.insert_at_last("c")

    with self.assertRaises(AttributeError):
      dq.find_middle()
    
if __name__ == '__main__':
  unittest.main(argv=['first-arg-is-ignored'], exit=False)
    
    
