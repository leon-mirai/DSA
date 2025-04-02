class SLLNODE:
    def __init__(self, value):
        self.value = value
        self.next = None

class SLLQueue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
        
    def peek(self):
        if self.is_empty():
            return "Empty"
        return self.first.value
        
    def enqueue(self, value):
        new_node = SLLNODE(value)
        if self.first == None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        
    def remove(self, index):
        if index < 0 or index >= self.length:
            return "Out of bounds"
        current = self.first
        previous = None
        count = 0
        while count is not index:
            previous = current
            current = current.next
            count += 1
        if (index == 0):
            self.first = current.next
            if self.first is None:
                self.last = None
        else:
            previous.next = current.next
            if current.next is None:
                self.last = previous
        self.length -= 1
        
    def dequeue(self):
        if self.is_empty():
            return "Empty"
        new_first = self.first
        self.first = new_first.next
        self.length -= 1
        
    def is_empty(self):
        return self.length == 0
    
    def print_list(self):
        current = self.first
        
        while current is not None:
            print(current.value, end=" --> ")
            current = current.next
        print("None")