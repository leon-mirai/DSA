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

my_linked_list = LinkedList()
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.print_list()

def reverse(linked_list):
    if linked_list.length <= 1:
        return 
    
    first = linked_list.head
    second = first.next
    linked_list.tail = linked_list.head
    while second:
        temp = second.next
        second.next = first
        first = second
        second = temp
    linked_list.head = first
    linked_list.tail.next = None
    return linked_list


reversed = reverse(my_linked_list)
reversed.print_list()



