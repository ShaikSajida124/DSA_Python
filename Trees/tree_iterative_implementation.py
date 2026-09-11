class EmptyStackError(IndexError):pass
class FullStackError(OverflowError):pass
class QueueUnderflowError(IndexError):pass
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

#Tree Implementation
class Node:
  def __init__(self, data, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

class BST:
  def __init__(self):
    self.root = None
    self.size = 0

  def is_empty(self):
    return self.root is None

  def __len__(self):
    return self.size

  def insert(self, item):
    node = Node(item)
    if self.is_empty():
      self.root = node
    else:
      current = self.root
      while current:
        if item == current.data:
          return
        elif item < current.data:
          if not current.left:
            current.left = node
            break
          else:
            current = current.left
        else:
          if not current.right:
            current.right = node
            break
          else:
            current = current.right
    self.size += 1

  def inorder_traverse(self):
    stack = Stack()
    current = self.root
    while current:
      stack.push(current)
      current = current.left
    while not stack.is_empty():
      temp = stack.pop()
      print(temp.data)
      if temp.right:
        rightTemp = temp.right
        while rightTemp:
          stack.push(rightTemp)
          rightTemp = rightTemp.left

  def search(self, data):
    current = self.root
    while current:
      if current.data == data:
        return current
      elif data < current.data:
        current = current.left
      else:
        current = current.right

  def preorder_traverse(self):
    stack = Stack()
    stack.push(self.root)
    while not stack.is_empty():
      current = stack.pop()
      print(current.data)
      if current.right:
        stack.push(current.right)
      if current.left:
        stack.push(current.left)

  '''def postOrder_traverse(self):
    stack = Stack()
    root_set = set()
    current = self.root
    while current:
      stack.push(current)
      current = current.left
    while not stack.is_empty():
      top = stack.peek()
      if top.right and (top.data not in root_set):
        root_set.add(top.data)
        rightTemp = top.right
        while rightTemp:
          stack.push(rightTemp)
          rightTemp = rightTemp.left
      else:
        temp = stack.pop()
        print(temp.data)
    '''

  def postorder_traverse(self):
    stack = Stack()
    current = self.root
    while current:
      stack.push(current)
      current = current.left
      
    processed_element = None
    while not stack.is_empty():
      top_element = stack.peek()
      if top_element.right and top_element.right != processed_element:
        temp = top_element.right
        while temp:
          stack.push(temp)
          temp = temp.left
      else:
        pop_element = stack.pop()
        processed_element = pop_element
        print(pop_element.data)

  def levelorder_traverse(self):
    if self.is_empty():
      return
    queue = Queue()
    queue.enqueue(self.root)
    while not queue.is_empty():
      current = queue.dequeue()
      print(current.data)
      if current.left:
        queue.enqueue(current.left)
      if current.right:
        queue.enqueue(current.right)

  def find_height(self, root):
    if root is None:
      return -1
    queue = Queue()
    queue.enqueue(root)
    height = -1
    length = 1
    while not queue.is_empty():
      for i in range(length):
        pop_element = queue.dequeue()
        if pop_element.left:
          queue.enqueue(pop_element.left)
        if pop_element.right:
          queue.enqueue(pop_element.right)
      length = len(queue)
      height += 1
    return height

  def find_minimum(self, root):
    if root is None:
      return
    while root.left:
      root = root.left
    return root

  def find_maximum(self, root):
    if root is None:
      return
    while root.right:
      root = root.right
    return root

  def delete_item(self, item):
    if self.is_empty():
      return
    par_ptr = None
    ptr = self.root
    while ptr:
      if item == ptr.data:
        break
      par_ptr = ptr
      if item < ptr.data:
        ptr = ptr.left
      else:
        ptr = ptr.right
    del_node_data = None
    if ptr:
      del_node_data = ptr.data
      if not ptr.left and not ptr.right:
        if ptr == self.root:
          self.root = None
        elif ptr.data < par_ptr.data:
          par_ptr.left = None
        else:
          par_ptr.right = None
      elif ptr.left and not ptr.right:
        if ptr == self.root:
          self.root = ptr.left
        else:
          if ptr.data < par_ptr.data:
            par_ptr.left = ptr.left
          else:
            par_ptr.right = ptr.left
      elif ptr.right and not ptr.left:
        if ptr == self.root:
          self.root = ptr.right
        else:
          if ptr.data < par_ptr.data:
            par_ptr.left = ptr.right
          else:
            par_ptr.right = ptr.right
      else:
        pred = self.find_maximum(ptr.left)
        ptr.data = pred.data
        par_pred = ptr
        pred = ptr.left
        while pred:
          if pred.data == ptr.data:
            break
          par_pred = pred
          if pred.data < ptr.data:
            pred = pred.left
          else:
            pred = pred.right
        if pred.left:
          if pred.data < par_pred.data:
            par_pred.left = pred.left
          else:
            par_pred.right = pred.left
        else:
          if pred.data < par_pred.data:
            par_pred.left = None
          else:
            par_pred.right = None
      self.size -= 1
      return del_node_data
          
  
        
bst = BST()
bst.insert(70)
bst.insert(60)
bst.insert(50)
bst.insert(65)
bst.insert(80)
bst.insert(75)
bst.insert(85)
bst.insert(90)
bst.insert(95)
bst.insert(45)
#bst.inorder_traverse()
#bst.preorder_traverse()
#bst.postorder_traverse()
bst.levelorder_traverse()
    
