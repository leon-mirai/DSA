from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
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
                if value < curr_node.value:
                    if not curr_node.left:
                        curr_node.left = new_node
                        return
                    curr_node = curr_node.left
                else:
                    if not curr_node.right:
                        curr_node.right = new_node
                        return
                    curr_node = curr_node.right

    def lookup(self, value):
        curr_node = self.root
        while curr_node:
            if curr_node.value == value:
                return True
            elif value < curr_node.value:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
        return False
    
    def print_tree(self, node=None, prefix="", is_left=True):
        if node is None:
            node = self.root
        
        if node.right:
            self.print_tree(node.right, prefix + ("│   " if is_left else "    "), False)
        
        print(prefix + ("└── " if is_left else "┌── ") + str(node.value))
        
        if node.left:
            self.print_tree(node.left, prefix + ("    " if is_left else "│   "), True)
        
    def breathFirstSearch(self):
        current_node = self.root
        list = []
        queue = []
        queue.append(current_node)
        
        while len(queue) > 0:
            current_node = queue.pop(0)
            list.append(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
            
        return list
    
    def DFSInOrder(self):
        return self.traverseInOrder(self.root, [])
    
    def traverseInOrder(self, node, list):
        if node.left:
            self.traverseInOrder(node.left, list)
        list.append(node.value)
        if node.right:
            self.traverseInOrder(node.right, list)
        return list
    
    
   
    # preorder [9, 4, 1, 6, 20, 15, 30] helps you remake tree    
    def DFSPreorder(self):
        return self.traversePreorder(self.root, [])
    
    def traversePreorder(self, node, list):
        list.append(node.value)
        if node.left:
            self.traversePreorder(node.left, list)
        if node.right:
            self.traversePreorder(node.right, list)
        return list
    # postorder [1, 6, 4, 15, 30, 20, 9] children come before parent    
    def DFSPostorder(self):
        return self.traversePostorder(self.root, [])
    
    def traversePostorder(self, node, list):
        
        if node.left:
            self.traversePostorder(node.left, list)
        if node.right:
            self.traversePostorder(node.right, list)
        list.append(node.value)
        return list

# Example Usage
tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(30)
tree.insert(15)
tree.insert(1)
tree.print_tree()
print(tree.DFSInOrder())
print(tree.DFSPreorder())
print(tree.DFSPostorder())