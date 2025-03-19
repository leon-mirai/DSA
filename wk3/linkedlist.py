class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        
        
    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            
        else:
            new_node.next = self.head
            self.head = new_node
        self.length = 1
            
        
    def insert(self, index, value):
        new_node = Node(value)
        current = self.head
        previous = None
        count = 0
        
        while count is not index:
            previous = current
            current = current.next
            count += 1
        new_node.next = current
        if (index == 0):
            self.head = None
        else: 
            previous.next = new_node
        self.length += 1
        
    def remove(self, index):
        current = self.head
        previous = None
        count = 0
        
        while count is not index:
            previous = current
            current = current.next
            count += 1
        if (index == 0):
            self.head = current.next
        else:
            previous.next = current.next
        self.length -= 1
    
    def print_list(self):
        current = self.head
        
        while current is not None:
            print(current.data, end=" --> ")
            current = current.next
        print("None")
        
        
linked_list = LinkedList()
linked_list.append(10)
linked_list.append(5)
linked_list.append(16)
linked_list.prepend(3)
linked_list.insert(1, 55)
linked_list.remove(1)
linked_list.print_list()
