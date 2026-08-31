class QueueUnderflowError(IndexError):
  pass
class QueueOverflowError(OverflowError):
  pass

class Queue(list):
  def __init__(self, capacity=None):
    if capacity is not None and not isinstance(capacity, int):
      raise TypeError("'Capacity' must be an 'integer'")
    self.capacity = capacity
    super().__init__()

  def __str__(self):
    if self.is_empty():
      return "List is empty"
    result = [str(item) for item in self]
    return f"=== QUEUE ITEMS ===\n[FRONT] {' -> '.join(result)} [REAR]"

  def is_empty(self):
    return len(self) == 0

  def is_full(self):
    if self.capacity is None:
      return False
    return len(self) >= self.capacity

  def enqueue(self, data):
    if self.is_full():
      raise QueueOverflowError("Cannot enqueue; 'Queue' is full")
    super().append(data)

  def dequeue(self):
    if self.is_empty():
      raise QueueUnderflowError("Cannot dequeue; 'Queue' is empty")
    return super().pop(0)

  def get_front(self):
    if self.is_empty():
      raise QueueUnderflowError("Cannot peek front; 'Queue' is empty")
    return super().__getitem__(0)

  def get_rear(self):
    if self.is_empty():
      raise QueueUnderflowError("Cannot peek rear; 'Queue' is empty")
    return super().__getitem__(-1)

  #RESTRICTED METHODS
  def append(self, *args, **kwargs):
   raise AttributeError("'Queue' has no attribute 'append'")

  def insert(self, *args, **kwargs):
    raise AttributeError("'Queue' has no attribute 'insert'")

  def extend(self, *args, **kwargs):
    raise AttributeError("'Queue' has no attribute 'extend'")

  def pop(self, *args, **kwargs):
    raise AttributeError("'Queue' has no attribute 'pop'")

  def remove(self, *args, **kwargs):
    raise AttributeError("'Queue' has no attribute 'remove'")

  def index(self, *args, **kwargs):
    raise AttributeError("'Queue' has no attribute 'index'")

  def count(self, *args, **kwargs):
    raise AttributeError("'Queue' has no attribute 'count'")

  def reverse(self, *args, **kwargs):
    raise AttributeError("'Queue' has no attribute 'reverse'")

  def sort(self, *args, **kwargs):
    raise AttributeError("'Queue' has no attribute 'sort'")

  def copy(self, *args, **kwargs):
    raise AttributeError("'Queue' has no attribute 'copy'")

  def __setitem__(self, *args, **kwargs):
    raise TypeError("'Queue' elements cannot be modified by index")

  def __delitem__(self, key):
    raise TypeError("'Queue' elements cannot be deleted by index")

  def __add__(self, others):
    raise AttributeError("Concat operator '+' not supported on 'Queue'")

  def __iadd__(self, others):
    raise AttributeError("In-place concat operator '+=' not supported on 'Queue'")

  def __mul__(self, others):
    raise AttributeError("Multiplication operator '*' not supported on 'Queue'")

  def __imul__(self, others):
    raise AttributeError("In-place multiplication operator '*=' not supported on 'Queue'")
    


q = Queue(capacity=10)

try:
  print('List is empty:', q.is_empty())
  print('List length:', len(q))
  q.enqueue(10)
  q.enqueue(20)
  q.enqueue(30)
  q.enqueue(40)
  print("Queue length after adding items to queue:", len(q))
  print("="*40)
  print(q)
  print("REAR:", q.get_rear())
  print("FRONT:", q.get_front())
  print("==========  deletion  ===========")
  print(q.dequeue())
  print(q.dequeue())
  print(q.dequeue())
  print(q.dequeue())
  print("list length after deletion:", len(q))
  print(q)
  print("=========  Exception Handling  ===========")
  q.enqueue("A")
  q.enqueue("B")
  q.enqueue("C")
  q.enqueue("D")
  q.enqueue("E")
  q.enqueue("F")
  print("Trying to call the restricted methods")
  q.insert(0, "a")
except AttributeError as A:
  print("Got AttributeError: ", A)
except TypeError as T:
  print("Got TypeError: ", T)
except QueueUnderflowError as U:
  print("QueueUnderflowError:", U)
except QueueOverflowError as O:
  print("QueueOverflowError:", O)

