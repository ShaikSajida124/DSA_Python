from sll_head_tail import *
class QueueUnderflowError(IndexError):
    pass
class QueueOverflowError(OverflowError):
    pass
class Queue(SLL):
    def __init__(self, capacity=None):
        self.capacity = capacity
        super().__init__()
    
    def __repr__(self):
        return f"Queue(size={len(self)})"
        
    def is_full(self):
        if self.capacity is None:
            return False
        return len(self) >= self.capacity
        
    def enqueue(self, data):
        if self.is_full():
            raise QueueOverflowError("Cannot enqueue; 'Queue' is full.")
        super().insert_at_last(data)
    
    def dequeue(self):
        if self.is_empty():
            raise QueueUnderflowError("Cannot dequeue; 'Queue' is empty.")
        return super().delete_first()
    
    def get_front(self):
        if self.is_empty():
            raise QueueUnderflowError("Cannot peek front; 'Queue' is empty.")
        return self.head.data
    
    def get_rear(self):
         if self.is_empty():
             raise QueueUnderflowError("Cannot peek rear; 'Queue' is empty.")
         return self.tail.data
     
    def insert_at_start(self, item):
         raise AttributeError("'Queue' object has no attribute 'insert_at_start'")
         
    def search(self, item):
         raise AttributeError("'Queue' object has no attribute 'search'")
    
    def insert_after(self, address, item):
         raise AttributeError("'Queue' object has no attribute 'insert_after'")
    
    def delete_last(self):
         raise AttributeError("'Queue' object has no attribute 'delete_last'")
     
    def delete_after(self, address):
         raise AttributeError("'Queue' object has no attribute 'delete_after'")
    
    def get_index(self, item):
         raise AttributeError("'Queue' object has no attribute 'get_index'")
     
    def get_item_at_index(self, index):
         raise AttributeError("'Queue' object has no attribute 'get_item_at_index'")
         
    def insert_at_index(self, index, item):
         raise AttributeError("'Queue' object has no attribute 'insert_at_index'")
    
    def delete_at_index(self, index):
         raise AttributeError("'Queue' object has no attribute 'delete_at_index'")
     
    def reverse_list(self):
         raise AttributeError("'Queue' object has no attribute 'reverse_list'")
     
    def check_and_fix_cycle(self):
         raise AttributeError("'Queue' object has no attribute 'check_and_fix_cycle'")
    
    def find_middle(self):
         raise AttributeError("'Queue' object has no attribute 'find_middle'")
    
    def delete_middle(self):
         raise AttributeError("'Queue' object has no attribute 'delete_middle'")
         
    def delete_first(self):
         raise AttributeError("'Queue' object has no attribute 'delete_first'")
    
    def insert_at_last(self, item):
         raise AttributeError("'Queue' object has no attribute 'insert_at_last'")
         
