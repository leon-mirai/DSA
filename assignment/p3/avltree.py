class Node:
    def __init__(self, data):
        self.data = data
        self.height = None
        self.lchild = None
        self.rchild = None
        
class AVLTree:
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root == new_node
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