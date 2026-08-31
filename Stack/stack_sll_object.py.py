from sll import SLL
class EmptyStackError(IndexError):pass
class FullStackError(OverflowError):pass
    
class Stack:
    def __init__(self):
        self.__items = SLL()
    
    def __str__(self):
        return f'{self.__items}'
    
    def __repr__(self):
        return f"Stack(size=({self.size()}))"
    
    def __iter__(self):
       current = self.__items.head
       while current:
          yield current.data
          current = current.next
        
    def is_empty(self):
        return self.__items.is_empty()
    
    def push(self, item):
        self.__items.insert_at_start(item)
    
    def pop(self):
       if self.is_empty():
           raise EmptyStackError("list is empty")
       del_node = self.__items.head.data
       self.__items.remove_at_start()
       return del_node
    
    def peek(self):
        if self.is_empty():
            raise EmptyStackError("list is empty")
        return self.__items.head.data
    
    def size(self):
        return len(self.__items)
    
    def clear(self):
        self.__items.clear()
        
