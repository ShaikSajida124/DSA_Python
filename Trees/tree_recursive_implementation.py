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
    if self.is_empty():
      self.root = node
      self.size += 1
    else:
      self.rinsert(self.root, node)

  def rinsert(self, root, node):
    if node.data == root.data:
      return
    elif node.data < root.data:
      if not root.left:
        root.left = node
        self.size += 1
      else:
        self.rinsert(root.left, node)
    else:
      if not root.right:
        root.right = node
        self.size += 1
      else:
        self.rinsert(root.right, node)

  #inorder traversal
  def inorder_traversal(self):
    self.rinorder_traversal(self.root)

  def rinorder_traversal(self, root):
    if root is None:
      return
    self.rinorder_traversal(root.left)
    print(root.data)
    self.rinorder_traversal(root.right)

  #preorder traversal
  def preorder_traversal(self):
    self.rpreorder_traversal(self.root)

  def rpreorder_traversal(self, root):
    if root is None:
      return
    print(root.data)
    self.rpreorder_traversal(root.left)
    self.rpreorder_traversal(root.right)

  #postorder traversal
  def postorder_traversal(self):
    self.rpostorder_traversal(self.root)

  def rpostorder_traversal(self, root):
    if root is None:
      return
    self.rpostorder_traversal(root.left)
    self.rpostorder_traversal(root.right)
    print(root.data)

  #This implementation is to count the node height.
  #If we want to count the edges we can just assume missing childs as -1 instead of 0.
  def find_height(self, root):
    if not root: 
      return 0
    return max(self.find_height(root.left) if root.left else 0, self.find_height(root.right) if root.right else 0) + 1


      

    
    
      
