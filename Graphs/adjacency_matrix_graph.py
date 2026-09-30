class EmptyStackError(IndexError):pass
class FullStackError(OverflowError):pass
class QueueUnderflowError(IndexError):pass
  
#stack
class StackNode:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class Stack:
  def __init__(self, capacity=None):
    self.start = None
    self.capacity = capacity
    self._size = 0

  def __iter__(self):
    current = self.start
    while current:
      yield current.data
      current = current.next

  def __str__(self):
    if self.is_empty():
      return "Stack is empty"
    stack_items = [str(item) for item in self]
    return f"=== STACK ITEMS ===\n{' -> '.join(stack_items)}"
    
  def __len__(self):
    return self._size

  def is_empty(self):
    return self.start is None

  def is_full(self):
    if self.capacity is None:
      return False
    return len(self) >= self.capacity

  def push(self, item):
    if self.is_full():
      raise FullStackError("'Stack' is full; cannot push an item")
    node = StackNode(item, self.start)
    self.start = node
    self._size += 1

  def pop(self):
    if self.is_empty():
      raise EmptyStackError("'Stack' is empty; cannot pop an item")
    deleted_item = self.start.data
    self.start = self.start.next
    self._size -= 1
    return deleted_item

  def peek(self):
    return self.start.data
    
#Queue
class QueueNode:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class Queue:
  def __init__(self):
    self.front = None
    self.rear = None
    self.size = 0

  def __len__(self):
    return self.size

  def is_empty(self):
    return self.front is None

  def enqueue(self, data):
    node = QueueNode(data)
    if self.is_empty():
      self.front = node
    else:
      self.rear.next = node
    self.rear = node
    self.size += 1

  def dequeue(self):
    if self.is_empty():
      raise QueueUnderflowError("Cannot delete an item; 'Queue' is empty")
    del_item = self.front.data
    if self.front == self.rear:
      self.front = self.rear = None
    else:
      self.front = self.front.next
    self.size -= 1
    return del_item

import unittest
class Graph:
  def __init__(self, vertex_count):
    self.adj_matrix = [[0 for j in range(vertex_count)] for i in range(vertex_count)]
    self.vertex_count = vertex_count

  def add_edge(self, u, v, weight=1):
   if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
     self.adj_matrix[u][v] = weight
     self.adj_matrix[v][u] = weight
   else:
     raise IndexError("Invalid vertex")

  def remove_edge(self, u, v):
    if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
      self.adj_matrix[u][v] = 0
      self.adj_matrix[v][u] = 0
    else:
      raise IndexError("Invalid vertex")
    
  def has_edge(self, u, v):
    if self.adj_matrix[u][v] > 0:
      return True
    return False
  def print_adj_matrix(self):
    for i in self.adj_matrix:
      print(i)
      
  def bfs(self):
    queue = Queue()
    visited_vertices = [False for i in range(self.vertex_count)]
    queue.enqueue(0)
    visited_vertices[0] = True
    while not queue.is_empty():
      current = queue.dequeue()
      print(current)
      adj_current = self.adj_matrix[current]
      for i in range(len(adj_current)):
        if adj_current[i] and visited_vertices[i] != True:
          queue.enqueue(i)
          visited_vertices[i] = True

  def dfs(self):
    stack = Stack()
    visited_vertices = [False for i in range(self.vertex_count)]
    stack.push(0)
    visited_vertices[0] = True
    while not stack.is_empty():
      current = stack.pop()
      print(current)
      adj_current = self.adj_matrix[current]
      for i in range(len(adj_current)):
        if adj_current[i] and visited_vertices[i] != True:
          stack.push(i)
          visited_vertices[i] = True
          

class testCode(unittest.TestCase):
  def test_AddingEdges(self):
    g = Graph(5)
    g.add_edge(0,4)
    g.add_edge(0,1)
    g.add_edge(1,3)
  def test_Exception(self):
    g = Graph(5)
    with self.assertRaises(IndexError):
      g.add_edge(0,5,15)
    with self.assertRaises(IndexError):
      g.add_edge(-1, 2)
  def test_Existence(self):
    g = Graph(4)
    g.add_edge(1, 2, 10)
    g.add_edge(0, 1, 5)
    g.add_edge(2, 3, 15)
    self.assertEqual(g.has_edge(1,3), False)
    self.assertEqual(g.has_edge(0, 1), True)
    self.assertEqual(g.has_edge(1, 2), True)

if __name__ == '__main__':
  unittest.main(argv=['first-arg-is-ignored'], exit=False)

    
    
    



