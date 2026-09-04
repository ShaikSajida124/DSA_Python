class Node:
  def __init__(self, data, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

class BST:
  def __init__(self):
    self.root = None
    self.size = 0

  def __len__(self):
    return self.size

  def is_empty(self):
    return self.root is None

  def insert(self, data):
    node = Node(data)
    self.__insert_helper(self.root, node)
  

  def __insert_helper(self, current, node):
    if current is None:
      self.root = node
      self.size += 1
    elif node.data == current.data:
      return
    elif node.data < current.data:
      if not current.left:
        current.left = node
        self.size += 1
      else:
        self.__insert_helper(current.left, node)
    else:
      if not current.right:
        current.right = node
        self.size += 1
      else:
        self.__insert_helper(current.right, node)

  def inorder_traverse(self, current):
    if current is None:
      return
    self.inorder_traverse(current.left)
    print(current.data)
    self.inorder_traverse(current.right)

  def preorder_traverse(self, current):
    if current is None:
      return 
    print(current.data)
    self.preorder_traverse(current.left)
    self.preorder_traverse(current.right)

  def postorder_traverse(self, current):
    if current is None:
      return
    self.postorder_traverse(current.left)
    self.postorder_traverse(current.right)
    print(current.data)

  def search(self, current, item):
    if not current or current.data == item:
      return current
    elif item < current.data:
      return self.search(current.left, item)
    else:
      return self.search(current.right, item)

      
