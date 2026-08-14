class EmptyStackError(IndexError):pass
  
class Stack(list):
  def __init__(self, *args, **kwargs):
    if args or kwargs:
      raise TypeError("'Stack' object cannot be initialized with data")
    super().__init__()

  def insert(self, *args, **kwargs):
    raise AttributeError("'Stack' object has no attribute 'insert'")

  def remove(self, *args, **kwargs):
    raise AttributeError("'Stack' object has no attribute 'remove'")

  def append(self, *args, **kwargs):
    raise AttributeError("'Stack' object has no attribute 'append'")

  def extend(self, *args, **kwargs):
    raise AttributeError("'Stack' object has no attribute 'extend'")

  def __setitem__(self, index, value):
    raise TypeError("'Stack' object does not support item assignment")

  def __delitem__(self, index):
    raise TypeError("'Stack' object does not support item deletion")

  def __add__(self, other):
    raise TypeError("Concat operator '+' not supported on 'Stack'")

  def __iadd__(self, other):
    raise TypeError("In-place concat operator '+=' not supported on 'Stack'")

  def __mul__(self, other):
    raise TypeError("Multiplication operator '*' not supported on 'Stack'")

  def __imul__(self, other):
    raise TypeError("In-place multiplication operator '*=' not supported on 'Stack'")

  def reverse(self):
    raise AttributeError("'Stack' object has no attribute 'reverse'")

  def sort(self):
    raise AttributeError("'Stack' object has no attribute 'sort'")

  def index(self, item):
    raise AttributeError("'Stack' object has no attribute 'index'")

  def copy(self):
    raise AttributeError("'Stack' object has no attribute 'copy'")

  def is_empty(self):
    return len(self) == 0
    
  def push(self, data):
    super().append(data)

  def peek(self):
    if self.is_empty():
      raise EmptyStackError("Stack is empty")
    return self[-1]
