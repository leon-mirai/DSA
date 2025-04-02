class ArrayQueue:
    def __init__(self):
        self.orders = []  # Array to store orders
        
    def enqueue(self, order):
        """Add a new order to the queue."""
        self.orders.append(order)
        print(f"Order added: {order}")
    
    def dequeue(self):
        """Process and remove the next order."""
        if self.is_empty():
            print("No orders pending!")
            return None
        order = self.orders.pop(0)
        print(f"Processing order: {order}")
        return order
    
    def peek(self):
        """View the next order without removing it."""
        if self.is_empty():
            print("Queue is empty")
            return None
        next_order = self.orders[0]
        print(f"Next order: {next_order}")
        return next_order
    
    def cancel(self, order):
        """Remove a specific order from the queue."""
        try:
            self.orders.remove(order)
            print(f"Cancelled order: {order}")
        except ValueError:
            print(f"Order {order} not found!")
    
    def is_empty(self):
        """Check if there are pending orders."""
        return len(self.orders) == 0


if __name__ == "__main__":
    print("=== Order Queue System ===")
    queue = ArrayQueue()
    
    # Test cases
    queue.enqueue("Burger")
    queue.enqueue("Pizza")
    queue.enqueue("Salad")
    queue.enqueue("Spider")
    print(queue.orders)
    queue.peek()          
    queue.dequeue() 
    queue.cancel("Pizza") 
    print(queue.orders)
    queue.is_empty()     
    
   