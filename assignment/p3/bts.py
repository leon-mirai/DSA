from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
      
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            curr_node = self.root
            while True:
                if value < curr_node.data:
                    if not curr_node.left:
                        curr_node.left = new_node
                        return
                    curr_node = curr_node.left
                else:
                    if not curr_node.right:
                        curr_node.right = new_node
                        return
                    curr_node = curr_node.right

    def lookup(self, data):
        curr_node = self.root
        while curr_node:
            if curr_node.data == data:
                return True
            elif data < curr_node.data:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
        return False
    
    def print_tree(self, node=None, prefix="", is_left=True):
        if node is None:
            node = self.root
        
        if node.right:
            self.print_tree(node.right, prefix + ("│   " if is_left else "    "), False)
        
        print(prefix + ("└── " if is_left else "┌── ") + str(node.data))
        
        if node.left:
            self.print_tree(node.left, prefix + ("    " if is_left else "│   "), True)

# Example Usage
tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(30)
tree.insert(15)
tree.insert(1)
tree.insert(20)
tree.insert(30)
tree.insert(15)
tree.insert(1)
tree.print_tree()