from sll_head import*
class EmptyStackError(IndexError):
    pass
class FullStackError(OverflowError):
    pass
    
class Stack(SLL):
    def __init__(self, capacity=None):
        self.__capacity = capacity 
        super().__init__()
       
    def is_full(self):
        if self.__capacity is None:
            return False
        return len(self) >= self.__capacity
    
    def push(self, data):
        if self.is_full():
            raise FullStackError("Cannot push an item; 'Stack' is full.")
        self.insert_at_start(data)
        
    def pop(self):
       if self.is_empty():
           raise EmptyStackError("Cannot pop an element; 'Stack' is empty.")
       return self.remove_at_start()
       
    def peek(self):
       if self.is_empty():
           raise EmptyStackError("Cannot peek; 'Stack' is empty.")
       return self.head.data
