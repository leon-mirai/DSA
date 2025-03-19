"""
Stack is empty is printed
Returns index error



"""

class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, item):
        self.stack.append(item)
        
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def __str__(self):
        return str(self.stack)
    
    def __iter__(self):
        return iter(self.stack)
    
    
myStack = Stack()

print(myStack.is_empty())
myStack.push(5)
myStack.push(10)
print(myStack)

for i in myStack:
    print(i)