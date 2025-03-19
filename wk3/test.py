class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0
    
    def append(self, item):
        new_node = Node(item)
        
        if (self.head is None):
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        

myLL = LinkedList()
myLL.append(5)
print(myLL)


    # def append(self):
        
    # def prepend(self):
        
    # def insert(self):
        
    # def remove(self):
        
    # def print_linked_list(self):
        