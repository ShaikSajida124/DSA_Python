class Deque:
  def __init__(self, capacity=None):
    self.capacity = capacity
    self.__items = DLL()

  def __len__(self):
    return len(self.__items)

  def __iter__(self):
    return iter(self.__items)

  def __str__(self):
    if self.is_empty():
      return "Deque is empty"
    result = [str(item) for item in self]
    return f"=== DEQUE ITEMS ===\n[FRONT] {' -> '.join(result)} [REAR]"

  def __repr__(self):
    return f"Deque(size={len(self)})"

  def is_empty(self):
    return self.__items.is_empty()

  def is_full(self):
    if self.capacity is None:
      return False
    return len(self) >= self.capacity

  def insert_at_front(self, item):
    if self.is_full():
      raise DequeOverFlowError("Cannot insert an item; 'Deque' is full")
    self.__items.insert_at_start(item)

  def insert_at_rear(self, item):
    if self.is_full():
      raise DequeOverFlowError("Cannot insert an item; 'Deque' is full")
    self.__items.insert_at_last(item)

  def delete_front(self):
    if self.is_empty():
      raise DequeUnderFlowError("Cannot delete an item; 'Deque' is empty")
    return self.__items.delete_first()

  def delete_rear(self):
    if self.is_empty():
      raise DequeUnderFlowError("Cannot delete an item; 'Deque' is empty")
    return self.__items.delete_last()

  def get_front(self):
    if self.is_empty():
      raise DequeUnderFlowError("Cannot peek front; 'Deque' is empty")
    return self.__items.head.data

  def get_rear(self):
    if self.is_empty():
      raise DequeUnderFlowError("Cannot peek rear; 'Deque' is empty")
    return self.__items.tail.data

  def clear(self):
    self.__items.clear()

#===========Test===============
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
    dq.insert_at_rear("B")
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
    
if __name__ == '__main__':
  unittest.main(argv=['first-arg-is-ignored'], exit=False)
    
    
