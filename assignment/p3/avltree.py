"""
node:
value, height, left, right

root
get_height
get_balance
root.height = 1 + max()
balance = get_balance()

left rotate

right rotate

LR rotate

RL rotate
"""
        
class Node:
    def __init__(self, value):
        self.value = value
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self):
        self.root = None
    
    def get_height(self, node):
        if not node:
            return 0
        return node.height
    
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
    
    def insert(self, root, value):
        if not root:
            return Node(value)
        elif value < self.root:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)
        
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and value < root.left.value:
            return 
        if balance < -1 and value > root.right.value:
            return

    

#     def insert(self, root, value):
#         if not root:
#             return Node(value)
#         elif value < root.value:
#             root.left = self.insert(root.left, value)
#         else:
#             root.right = self.insert(root.right, value)

#         root.height = 1 + max(self.height(root.left), self.height(root.right))
#         balance = self.balance(root)

#         # Left rotation
#         if balance > 1 and value < root.left.value:
#             return self.right_rotate(root)

#         # Right rotation
#         if balance < -1 and value > root.right.value:
#             return self.left_rotate(root)

#         # Left-Right rotation
#         if balance > 1 and value > root.left.value:
#             root.left = self.left_rotate(root.left)
#             return self.right_rotate(root)

#         # Right-Left rotation
#         if balance < -1 and value < root.right.value:
#             root.right = self.right_rotate(root.right)
#             return self.left_rotate(root)

#         return root

#     def delete(self, root, value):
#         if not root:
#             return root

#         if value < root.value:
#             root.left = self.delete(root.left, value)
#         elif value > root.value:
#             root.right = self.delete(root.right, value)
#         else:
#             if not root.left:
#                 temp = root.right
#                 root = None
#                 return temp
#             elif not root.right:
#                 temp = root.left
#                 root = None
#                 return temp

#             temp = self.min_value_node(root.right)
#             root.value = temp.value
#             root.right = self.delete(root.right, temp.value)

#         if not root:
#             return root

#         root.height = 1 + max(self.height(root.left), self.height(root.right))
#         balance = self.balance(root)

#         # Left rotation
#         if balance > 1 and self.balance(root.left) >= 0:
#             return self.right_rotate(root)

#         # Right rotation
#         if balance < -1 and self.balance(root.right) <= 0:
#             return self.left_rotate(root)

#         # Left-Right rotation
#         if balance > 1 and self.balance(root.left) < 0:
#             root.left = self.left_rotate(root.left)
#             return self.right_rotate(root)

#         # Right-Left rotation
#         if balance < -1 and self.balance(root.right) > 0:
#             root.right = self.right_rotate(root.right)
#             return self.left_rotate(root)

#         return root

#     def left_rotate(self, z):
#         y = z.right
#         T2 = y.left

#         y.left = z
#         z.right = T2

#         z.height = 1 + max(self.height(z.left), self.height(z.right))
#         y.height = 1 + max(self.height(y.left), self.height(y.right))

#         return y

#     def right_rotate(self, z):
#         y = z.left
#         T3 = y.right

#         y.right = z
#         z.left = T3

#         z.height = 1 + max(self.height(z.left), self.height(z.right))
#         y.height = 1 + max(self.height(y.left), self.height(y.right))

#         return y

#     def min_value_node(self, root):
#         current = root
#         while current.left:
#             current = current.left
#         return current

#     def search(self, root, value):
#         if not root or root.value == value:
#             return root
#         if root.value < value:
#             return self.search(root.right, value)
#         return self.search(root.left, value)

#     def insert_value(self, value):
#         self.root = self.insert(self.root, value)

#     def delete_value(self, value):
#         self.root = self.delete(self.root, value)

#     def search_value(self, value):
#         return self.search(self.root, value)

#     # New method to print the tree
#     def print_tree(self, node=None, prefix="", is_left=True):
#         if node is None:
#             node = self.root
        
#         if node.right:
#             self.print_tree(node.right, prefix + ("│   " if is_left else "    "), False)
        
#         print(prefix + ("└── " if is_left else "┌── ") + str(node.value))
        
#         if node.left:
#             self.print_tree(node.left, prefix + ("    " if is_left else "│   "), True)

# # Example usage:
# if __name__ == "__main__":
#     tree = AVLTree()
#     tree.insert_value(10)
#     tree.insert_value(20)
#     tree.insert_value(30)
#     tree.insert_value(40)
#     tree.insert_value(50)

#     print("Tree after insertion:")
#     # Print the tree structure
#     tree.print_tree()

#     tree.delete_value(20)
#     print("Tree after deletion of 20:")
#     tree.print_tree()

#     result = tree.search_value(30)
#     if result:
#         print("Node found")
#     else:
#         print("Node not found")
