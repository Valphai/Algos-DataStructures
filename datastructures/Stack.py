from .nodes.SimpleNode import Node as Node

class Stack():
    def __init__(self):
        self.top = None
        self.size = 0
        
    def __len__(self):
        return self.size
        
    def push(self, value):
        node = Node(value)
        if len(self) == 0:
            self.top = node
        else:
            node.next_node = self.top
            self.top = node
        self.size += 1
        
    def pop(self):
        if len(self) == 0:
            raise Exception("Stack is empty")
        else:
            last_one = self.top
            self.top = self.top.next_node
            self.size -= 1
        return last_one.data
        
    def peek(self):
        return self.top.data