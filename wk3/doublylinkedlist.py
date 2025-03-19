class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
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
            self.head.prev = new_node
            self.head = new_node
        self.length = 1
            
    def insert(self, index, value):
        if index < 0 or index > self.length:
            raise IndexError("Index out of bounds")
        new_node = Node(value)
        
        if index == 0:
            self.prepend(value)
            return
        if index == self.length:
            self.append(value)
            return
        current = self.head
        for _ in range(index - 1):
            current = current.next
        new_node.next = current.next
        new_node.prev = current
        current.next.prev = new_node
        current.next = new_node
        self.length += 1
        
    def remove(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of bounds")

        if index == 0:
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
        else:
            current = self.head
            for _ in range(index):
                current = current.next

            if index == self.length - 1:
                self.tail = current.prev
                self.tail.next = None
            else:
                current.prev.next = current.next
                current.next.prev = current.prev

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

linked_list.print_list()
