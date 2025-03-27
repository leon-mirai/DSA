class ArrayQueue:
    def __init__(self):
        self.queue = []        
    
    def enqueue(self,value):
        self.queue.append(value)
        print(f"Appended value: {value}")
    
    def dequeue(self):
        deqed_element = self.queue.pop(0)
        print(f"Dequeued Element: {deqed_element}")
        return deqed_element        
    def remove(self, index):
        removed = self.queue.pop(index)
        print(f"Removed element at index: {removed}")

    def peek(self):
        if self.is_empty():
            return "Empty"
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0
    
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

class DLLNODE:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DLLQueue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
        
    def peek(self):
        if self.is_empty():
            return "Empty"
        return self.first.value
        
    def enqueue(self, value):
        new_node = DLLNODE(value)
        if self.first == None:
            self.first = new_node
            self.last = new_node
        else:
            new_node.prev = self.last
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        
    def insert(self, index, value):
        new_node = DLLNODE(value)
        if index < 0 or index > self.length:
            return
        
        if index == 0:
            if self.first is None:
                self.first = new_node
                self.last = new_node
            else:
                new_node.next = self.first
                self.first.prev = new_node
                self.first = new_node
        else:
            current = self.first
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            if current.next:
                current.next.prev = new_node
            new_node.prev = current
            current.next = new_node
            
            if new_node.next is None:
                self.last = new_node
            
            
        
    def remove(self, index):
        if index < 0 or index >= self.length:
            return
        
        current = self.first
        
        for i in range(index):
            current = current.next
        
        if current == self.first:
            self.first = current.next
            if self.first:
                self.first.prev = None
        elif current == self.last:
            self.last = current.prev
            if self.last:
                self.last.next = None
        else:
            current.prev.next = current.next
            current.next.prev = current.prev
        
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



myQ = DLLQueue()
myQ.enqueue(7)
myQ.enqueue(9)
myQ.enqueue(3)
myQ.insert(1,4)


myQ.print_list()