from .nodes.SimpleNode import Node as Node

class Queue():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def __len__(self):
        return self.size
    
    def peek(self):
        return self.size
    
    def is_empty(self):
        return len(self) == 0 
        
    def dequeue(self):
        self.size -= 1
        if self.is_empty():
            raise Exception("Queue is empty, len = {}".format(self.size))
        else:
            current = self.head.data
            self.head = self.head.next_node
            return current
        
    def enqueue(self, value):
        self.size += 1
        node = Node(value)
        if self.is_empty():
            self.head = node
            self.tail = node