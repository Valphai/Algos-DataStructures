from .nodes.BBSTNode import Node as Node

class AVLTree():
    def __init__(self):
        self.root = None

    def contains(self, value) -> bool:
        return self._contains(self.root, value)

    def _contains(self, node, value) -> bool:
        if self.node == None:
            return False
        
        if node.value < value:
            return self._contains(node.left, value)
        
        elif node.value > value:
            return self._contains(node.right, value)
        
        else:
            return True

    def insert(self, value) -> bool:
        if not self.contains(value):
            self.root = self._insert(self.root, value)
            return True

        return False

    def _insert(self, node, value) -> Node:
        if node == None:
            return Node()
        
        if node.value < value:
            node.left = self._insert(node.left, value)
        
        elif node.value > value:
            node.right = self._insert(node.right, value)

        self.update(node)

        return self.balance(node)

    def update(self, node):
        lh, rh = -1, -1
        if node.left is not None:
            lh = node.left.height
        if node.right is not None:
            rh = node.right.height

        node.height = 1 + max(lh, rh)
        
        node.BF = rh - lh
        
    def balance(self, node) -> Node:
        if node.BF == -2:
            if node.left.BF <= 0:
                return self.left_left(node)

            else:
                return self.left_right(node)

        if node.BF == 2:
            if node.right.BF >= 0:
                return self.right_right(node)

            else:
                return self.right_left(node)
        
        return node


    def left_left(self, node):
        return self.right_rotation(node)

    def left_right(self, node):
        node.left = self.left_rotation(node.left)
        return self.left_left(node)

    def right_right(self, node):
        return self.left_rotation(node)

    def right_left(self, node):
        node.right = self.right_rotation(node.right)
        return self.right_right(node)

    def right_rotation(self, node):
        left_node = node.left
        node.left = left_node.right
        left_node.right = node

        self.update(node)
        self.update(left_node)

        return left_node

    def left_rotation(self, node):
        right_node = node.right
        node.right = right_node.left
        right_node.left = node

        self.update(node)
        self.update(right_node)

        return right_node

    def remove(self, value):
        if self.contains(self.root, value):
            self.root = self._remove(self.root, value)
            
    def _remove(self, node, value) -> Node:
        if node is None:
            return None
        
        if node.right.value < value:
            node.left = self._remove(node.left, value)
        
        elif node.left.value > value:
            node.right = self._remove(node.right, value)
        
        else: # node.value == value
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
                node.value = temp.value
                node.right = self._remove(node.right, temp.value)

        self.update(node)

        return self.balance(node)

    def dig_left(self, node):
        curr = node
        while curr.left != None:
            curr = curr.left

        return curr