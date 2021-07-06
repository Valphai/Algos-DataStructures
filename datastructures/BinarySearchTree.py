from .nodes.TreeNode import Node as Node

class BinarySearchTree():
    """
    works for non repeating elems
    """
    def __init__(self, array):
        self.root = None
        for i in array:
            self.add(i)

    def contains(self, elem):
        return self._contains(elem, self.root)

    def _contains(self, elem, node):
        if node is None:
            return False
        
        if node.data < elem:
            return self._contains(elem, node.right)

        elif node.data > elem:
            return self._contains(elem, node.left)

        else: # node.data == elem
            return True
    
    def add(self, elem):
        if self.contains(elem):
            return 
        
        else:
            self.root = self._add(elem, self.root)

        return 

    def _add(self, elem, node):
        if node is None:
            return Node(elem)
            
        else:
            if node.data < elem:
                node.right = self._add(elem, node.right)
            
            else:
                node.left = self._add(elem, node.left)
        
        return node
        
    def remove(self, elem):
        if self.contains(elem):
            self.root = self._remove(elem, self.root)

    def _remove(self, elem, node):
        if node is None:
            return None

        if node.data < elem:
            node.right = self._remove(elem, node.right)
        
        elif node.data > elem:
            node.left = self._remove(elem, node.left)
        
        else: # node.data == elem
            if node.right is None:
                left_child = node.left
                node = None

                return left_child

            elif node.left is None:
                right_child = node.right
                node = None
                
                return right_child

            else:
                temp = self.dig_left(node.right)
                node.data = temp.data
                node.right = self._remove(temp.data, node.right)
        
        return node

    def dig_left(self, node):
        curr = node
        while curr.left != None:
            curr = curr.left
        
        return curr
    
    def order_traverse(self, node):
        if node is None:
            return 
        print(node.data)
        self.order_traverse(node.left)
        self.order_traverse(node.right)