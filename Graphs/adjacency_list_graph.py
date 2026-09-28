class Graph:
  def __init__(self, vertex_count):
    self.adj_list = {vertex:[] for vertex in range(vertex_count)}
    self.vertex_count = vertex_count

  def add_edge(self, u, v, weight=1):
    if u in self.adj_list and v in self.adj_list:
      if self.has_edge(u, v):
        return
      self.adj_list[u].append((v, weight))
      self.adj_list[v].append((u, weight))
    else:
      raise IndexError("Invalid vertex")

  def remove_edge(self, u, v):
    if u in self.adj_list and v in self.adj_list:
      adj_u = self.adj_list[u]
      adj_v = self.adj_list[v]
      for i in range(len(adj_u)):
        if adj_u[i][0] == v:
          adj_u.pop(i)
          break
      for i in range(len(adj_v)):
        if adj_v[i][0] == u:
          adj_v.pop(i)
          break
    else:
      raise IndexError('Invalid vertex')

  def has_edge(self, u, v):
    if u in self.adj_list and v in self.adj_list:
      for vertex, weight in self.adj_list[u]:
        if vertex == v:
          return True
      return False
    else:
      raise IndexError("Invalid vertex")

  def print_adj_list(self):
    for vertex, n in self.adj_list.items():
      print(f'v {vertex} : {n}')
          

      

g = Graph(4)
g.add_edge(0, 2, 10)
g.add_edge(1,2,5)
g.add_edge(2, 3, 11)
g.add_edge(0, 1, 4)
g.add_edge(1,2)
g.print_adj_list()
