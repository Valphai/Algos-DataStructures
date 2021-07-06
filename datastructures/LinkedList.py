from .nodes.SimpleNode import Node as Node

class Linked_list():
    def __init__(self):
        self.head = None
    
    def __repr__(self):
        nodes = []
        current = self.head
        
        while current:
            if current is self.head:
                nodes.append("head {}:{}->".format(current, current.data))
            elif current.next_node is None:
                nodes.append("{} : {} tail".format(current, current.data))
            else:
                nodes.append("{} : {}->".format(current, current.data))
            
            current = current.next_node
        return "->".join(nodes)
    
    def __len__(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count
    
    def is_empty(self):
        return self.head == None
    
    def prepend(self, value):
        new_node = Node(value)
        new_node.next_node = self.head
        self.head = new_node
        
    def insert(self, value, index):
        current = self.head
        if index == 0:
            self.prepend(value)
        else:
            while index > 1:
                index -= 1
                current = current.next_node
            
            new_node = Node(value)
            previous = current
            next_node = current.next_node
            previous.next_node = new_node
            new_node.next_node = next_node
        
    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None
    
    def remove(self, key):
        found = False
        current = self.head
        previous = None
        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        return current