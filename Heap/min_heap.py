class EmptyHeapException(IndexError):pass

class MinHeap:
  def __init__(self):
    self.heap = []

  def __len__(self):
    return len(self.heap)

  def is_empty(self):
    return len(self) == 0

  def insert(self, item):
    self.heap.append(item)
    
    childIdx = len(self)-1
    parentIdx = (childIdx-1)//2
    
    while childIdx > 0 and self.heap[parentIdx] > self.heap[childIdx]:
      
      self.heap[parentIdx], self.heap[childIdx] = self.heap[childIdx], self.heap[parentIdx]
      
      childIdx = parentIdx
      parentIdx = (childIdx-1)//2

  def create_heap(self, arr):
    for item in arr:
      self.insert(item)

  def delete(self):
    if self.is_empty():
      raise EmptyHeapException("Heap is empty")
      
    if len(self) == 1:
      return self.heap.pop()
      
    del_item = self.heap[0]
    self.heap[0] = self.heap[-1]
    self.heap.pop()

    parentIdx = 0
    leftChildIdx = min(1, len(self)-1)
    rightChildIdx = min(2, len(self)-1)
    leastChildIdx = leftChildIdx if self.heap[leftChildIdx] < self.heap[rightChildIdx] else rightChildIdx

    while self.heap[parentIdx] > self.heap[leastChildIdx]:
      
      self.heap[parentIdx], self.heap[leastChildIdx] = self.heap[leastChildIdx], self.heap[parentIdx]
      
      parentIdx = leastChildIdx
      leftChildIdx = parentIdx*2+1
      rightChildIdx = parentIdx*2+2

      if leftChildIdx < len(self) and rightChildIdx < len(self):
        leastChildIdx = leftChildIdx if self.heap[leftChildIdx] < self.heap[rightChildIdx] else rightChildIdx
      elif leftChildIdx < len(self) or rightChildIdx < len(self):
        leastChildIdx = leftChildIdx if leftChildIdx < len(self) else rightChildIdx
      else:
        break
    return del_item

  def top(self):
    if self.is_empty():
      raise EmptyHeapException("Heap is empty")
    return self.heap[0]

  def heap_sort(self, arr):
    temp_heap = MinHeap()
    temp_heap.create_heap(arr)
    sorted_heap = []
    while not temp_heap.is_empty():
      sorted_heap.append(temp_heap.delete())
    return sorted_heap
  
