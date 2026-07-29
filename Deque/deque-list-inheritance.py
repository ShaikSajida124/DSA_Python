import unittest
class DequeUnderFlowError(IndexError):
  pass
class DequeOverFlowError(OverflowError):
  pass
  
#Deque implementation by inheriting list
class Deque(list):
  def __init__(self, capacity=None):
    if capacity is not None and (not isinstance(capacity, int) or capacity <= 0):
      raise TypeError("'capacity' must be an integer > 0")
    self.capacity = capacity
    super().__init__()

  def __str__(self):
    if self.is_empty():
      return "Deque is empty"
    result = [str(item) for item in self]
    return f"=== DEQUE ITEMS ===\n[FRONT] {' -> '.join(result)} [REAR]"

  def is_empty(self):
    return len(self) == 0

  def is_full(self):
    if self.capacity is None:
      return False
    return len(self) >= self.capacity

  def insert_at_front(self, data):
    if self.is_full():
      raise DequeOverFlowError("Cannot insert an element; 'Deque' is full")
    super().insert(0, data)

  def insert_at_rear(self, data):
    if self.is_full():
      raise DequeOverFlowError("Cannot insert an element; 'Deque' is full")
    super().append(data)

  def delete_front(self):
    if self.is_empty():
      raise DequeUnderFlowError("Cannot delete an item; 'Deque' is empty")
    return super().pop(0)

  def delete_rear(self):
    if self.is_empty():
      raise DequeUnderFlowError("Cannot delete an item; 'Deque' is empty")
    return super().pop()

  def get_front(self):
    if self.is_empty():
      raise DequeUnderFlowError("Cannot peek front; 'Deque' is empty")
    return super().__getitem__(0)

  def get_rear(self):
    if self.is_empty():
      raise DequeUnderFlowError("Cannot peek rear; 'Deque' is empty")
    return super().__getitem__(-1)

  #Restricted Methods
  def append(self, *args, **kwargs):
    raise AttributeError("'Deque' has no attribute 'append'")

  def insert(self, *args, **kwargs):
    raise AttributeError("'Deque' has no attribute 'insert'")

  def extend(self, *args, **kwargs):
    raise AttributeError("'Deque' has no attribute 'extend'")

  def pop(self, *args, **kwargs):
    raise AttributeError("'Deque' has no attribute 'pop'")

  def remove(self, *args, **kwargs):
    raise AttributeError("'Deque' has no attribute 'remove'")

  def index(self, *args, **kwargs):
    raise AttributeError("'Deque' has no attribute 'index'")

  def count(self, *args, **kwargs):
    raise AttributeError("'Deque' has no attribute 'count'")

  def reverse(self, *args, **kwargs):
    raise AttributeError("'Deque' has no attribute 'reverse'")

  def sort(self, *args, **kwargs):
    raise AttributeError("'Deque' has no attribute 'sort'")

  def copy(self, *args, **kwargs):
    raise AttributeError("'Deque' has no attribute 'copy'")

  def __setitem__(self, *args, **kwargs):
    raise TypeError("'Deque' elements cannot be modified by index")

  def __delitem__(self, key):
    raise TypeError("'Deque' elements cannot be deleted by index")

  def __add__(self, others):
    raise TypeError("Concat operator '+' not supported on 'Deque'")

  def __iadd__(self, others):
    raise TypeError("In-place concat operator '+=' not supported on 'Deque'")

  def __mul__(self, others):
    raise TypeError("Multiplication operator '*' not supported on 'Deque'")

  def __imul__(self, others):
    raise TypeError("In-place multiplication operator '*=' not supported on 'Deque'")


class myDeque(unittest.TestCase):
  def test_code(self):
    dq = Deque()
    self.assertTrue(dq.is_empty(), True)
    self.assertFalse(dq.is_full(), False)

    dq.insert_at_front(10)
    dq.insert_at_rear(20)
    dq.insert_at_rear(30)

    self.assertEqual(dq.get_front(), 10)
    self.assertEqual(dq.get_rear(), 30)

    self.assertEqual(dq.delete_front(), 10)
    self.assertEqual(dq.delete_rear(), 30)

    self.assertEqual(dq.get_rear(), 20)
    
  def test_underflow_exception(self):
    dq = Deque()

    with self.assertRaises(DequeUnderFlowError):
      dq.delete_front()
    with self.assertRaises(DequeUnderFlowError):
      dq.delete_rear()
    with self.assertRaises(DequeUnderFlowError):
      dq.get_rear()

  def test_overflow_exception(self):
    with self.assertRaises(TypeError):
      Deque(0)
    with self.assertRaises(TypeError):
      Deque(-10)
    with self.assertRaises(TypeError):
      Deque("five")

    dq = Deque(2)
    dq.insert_at_front(10)
    dq.insert_at_rear(20)

    self.assertTrue(dq.is_full())
    with self.assertRaises(DequeOverFlowError):
      dq.insert_at_front(30)

  def test_string_formatting(self):
    dq = Deque()
    self.assertEqual(str(dq), "Deque is empty")

    dq.insert_at_rear(10)
    dq.insert_at_rear(20)

    expected_output = "=== DEQUE ITEMS ===\n[FRONT] 10 -> 20 [REAR]"
    self.assertEqual(str(dq), expected_output)

  def test_blocked_mutator_methods(self):
    dq = Deque()
    dq.insert_at_front(10)
    with self.assertRaises(AttributeError):
      dq.append(10)

    with self.assertRaises(AttributeError):
      dq.insert(2, 20)

    with self.assertRaises(AttributeError):
      dq.pop(0)

    with self.assertRaises(AttributeError):
      dq.remove(0)

  def test_block_utility_methods(self):
    dq = Deque()
    dq.insert_at_front(10)

    with self.assertRaises(AttributeError):
      dq.sort()

    with self.assertRaises(AttributeError):
      dq.reverse()

    with self.assertRaises(AttributeError):
      dq.count()

    with self.assertRaises(AttributeError):
      dq.copy()

    with self.assertRaises(AttributeError):
      dq.index()
      
  def test_blocked_operators_and_indexing(self):
    dq = Deque()
    dq.insert_at_front(10)

    with self.assertRaises(TypeError):
      dq[0] = 5

    with self.assertRaises(TypeError):
      dq += [1, 2]

    with self.assertRaises(TypeError):
      dq = dq + [5, 6]

    with self.assertRaises(TypeError):
      dq *= 2

    with self.assertRaises(TypeError):
      dq = dq * 2
      

if __name__ == '__main__':
  unittest.main(argv=['first-arg-is-ignored'], exit=False)
  
