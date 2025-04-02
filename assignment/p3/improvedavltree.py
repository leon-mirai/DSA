class AVLNode:
    def __init__(self, value):
        self.value = value
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self):
        self.root = None
    
    def get_height(self, node):
        if node is None:
            return 0
        return node.height
    
    def get_balance_factor(self, node):
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
    
    def insert_value(self, value):
        self.root = self.__insert(self.root, value)
    
    def __insert(self, root, value):
        if root is None:
            return AVLNode(value)
        elif value < root.value:
            root.left = self.__insert(root.left, value)
        else:
            root.right = self.__insert(root.right, value)
        
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance_factor = self.get_balance_factor(root)
        # Right rotation (left-left case)
        if balance_factor > 1 and value < root.left.value:
            return self.rotate_right(root)
        # Left rotation (right-right case)
        if balance_factor < -1 and value > root.right.value:
            return self.rotate_left(root)
        # left-right rotation (left-right case)
        if balance_factor > 1 and value > root.left.value:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        # right-left rotation (right-left case)
        if balance_factor < -1 and value < root.right.value:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)
        
        return root
    
    def rotate_left(self, node):
        new_root = node.right
        left_subtree = new_root.left
        
        new_root.left = node
        node.right = left_subtree
        
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))
        
        return new_root
    
    def rotate_right(self, node):
        new_root = node.left
        right_subtree = new_root.right
        
        new_root.right = node
        node.left = right_subtree
        
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))
        
        return new_root

    def remove(self, value):
        self.root = self.__remove(self.root, value)

    def __remove(self, node, value):
        if node is None:
            return node
        
        # Traverse left or right
        if value < node.value:
            node.left = self.__remove(node.left, value)
        elif value > node.value:
            node.right = self.__remove(node.right, value)
        else:
            # Node with one child or no child
            if node.left is None:
                return node.right # give right node or None
            elif node.right is None:
                return node.left
            # Node with two children
            temp = self.__min_value_node(node.right) # right-left in-order successor
            node.value = temp.value
            node.right = self.__remove(node.right, temp.value)

        if node is None:
            return node

        # update height
        node.height = 1 + max(self.get_height(node.left),
                            self.get_height(node.right))

        # rebalance
        balance = self.get_balance_factor(node)
        # Left-Left
        if balance > 1 and self.get_balance_factor(node.left) >= 0:
            return self.rotate_right(node)
        # Right-Right
        if balance < -1 and self.get_balance_factor(node.right) <= 0:
            return self.rotate_left(node)
        # Left-Right
        if balance > 1 and self.get_balance_factor(node.left) < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        # Right-Left
        if balance < -1 and self.get_balance_factor(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def __min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    

    def search(self, target):
        current = self.root
        closest = None
        
        while current:
            if closest is None or abs(current.value - target) < abs(closest - target):
                closest = current.value
            elif abs(current.value - target) == abs(current.value - closest):
                closest = min(current.value, closest)
                
            if target < current.value:
                current = current.left
            elif target > current.value:
                current = current.right
            else:
                print("Exact:", current.value)
                return current.value
        print("Closest:", closest)
        return closest
    
    def print_tree(self, node=None, prefix="", is_left=True):
        if node is None:
            node = self.root
        
        if node.right:
            self.print_tree(node.right, prefix + ("│   " if is_left else "    "), False)
        
        print(prefix + ("└── " if is_left else "┌── ") + str(node.value))
        
        if node.left:
            self.print_tree(node.left, prefix + ("    " if is_left else "│   "), True)

class HashMap:
    def __init__(self):
        self.avl_tree = AVLTree()
        self.hash_map = dict() 
           
    def add_item(self, weight):
        self.avl_tree.insert_value(weight)
        self.hash_map[weight] = self.hash_map.get(weight, 0) + 1
        
    def remove_item(self, weight):
        if weight in self.hash_map:
            self.hash_map[weight] -= 1
            if self.hash_map[weight] == 0:
                del self.hash_map[weight]
            self.avl_tree.remove(weight)
            return True
        return False
            
    def search_item(self, target):
        if target in self.hash_map:
            print("Exact match:", target)
            return target
        
        closest = self.avl_tree.search(target)
        print("Closest match:", closest)
        return closest
    
warehouse = HashMap()
warehouse.add_item(4)
warehouse.add_item(10)
warehouse.add_item(17)
warehouse.add_item(22)
warehouse.search_item(22)
