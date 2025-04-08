# make node
class AVLNode:
    def __init__(self, value):
        self.value = value
        self.height = 1
        self.left = None
        self.right = None
# make avl tree
class AVLTree:
    def __init__(self):
        self.root = None
    
    def get_height(self, node):
        if node is None:
            return 0
        return node.height

    def get_balance(self, node):
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
    
    def __insert(self, root, value):
        if root is None:
            return AVLNode(value)
        if value < root.value:
            root.left = "go left"
        elif value > root.value:
            root.right = "go right"
        
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)
            
        


# make hash map
