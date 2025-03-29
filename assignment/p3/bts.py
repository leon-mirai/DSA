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
        self.root = new_node
        return
    
    def lookup(self, value):
        return
    
    def remove(self, value):
        return
    
    def traverse(self, node):
        if node is not None:
            self.traverse(node.left)
            print(node.data, end=" ")
            self.traverse(node.right)
    
    def print_tree(self):
        self.traverse(self.root)
        print()


tree = BinarySearchTree()
tree.insert(9)
tree.print_tree
# tree.insert(4)
# tree.insert(6)
# tree.insert(20)
# tree.insert(170)
# tree.insert(15)
# tree.insert(1)

# def r_search(node, key):
#     if node == None:
#         return None
#     if key == node.data:
#         return node
#     elif key < node.data:
#         return r_search(node.lchild, key)
#     else:
#         return r_search(node.rchild, key)
    
# def search(node, key):
#     while (node != None):
#         if key == node.data:
#             return node
#         elif key < node.data:
#             node = node.lchild
#         else:
#             node = node.rchild
            