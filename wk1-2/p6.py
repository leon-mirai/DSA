class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop()
        return "Queue is empty"
    
    def is_empty(self):
        return len(self.queue) == 0
    
# O(n) because when you pop an item, you have to shift everything to the left