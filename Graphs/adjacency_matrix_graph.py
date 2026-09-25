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
    
  def has_edge(self, vertex1, vertex2):
    if self.adj_matrix[vertex1][vertex2] > 0 and self.adj_matrix[vertex2][vertex1] > 0:
      return True
    return False

  def print_adj_matrix(self):
    for i in self.adj_matrix:
      print(i)

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

    
    
    



