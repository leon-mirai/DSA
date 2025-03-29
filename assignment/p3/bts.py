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
                    #left
                    if not curr_node.left:
                        curr_node.left = new_node
                        return
                    curr_node = curr_node.left
                else:
                    if not curr_node.right:
                        curr_node.right = new_node
                        return
                    curr_node = curr_node.right
        

    
    def lookup(self,data):
        curr_node = self.root
        while True:
            if curr_node == None:
                return False
            if curr_node.data == data:
                return True
            elif data < curr_node.data:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
                
    def remove(self, value):
        curr_node = self.root
        while True:
            if curr_node == None:
                return 
            if curr_node.data == value:
                return
            elif 
            

    
    def traverse(self, node):
        if node is not None:
            self.traverse(node.left)
            print(f"[{node.data}]", end=" ")
            self.traverse(node.right)
    
    def print_tree(self):
        self.traverse(self.root)
        print()


tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(30)
tree.insert(15)
tree.insert(1)
print(tree.lookup(1))
print(tree.lookup(17))
tree.print_tree()
