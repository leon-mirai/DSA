def max_heapify(A, heap_size, i):
    # Calculate left and right child indices
    left = 2 * i + 1 # line 15
    right = 2 * i + 2 # line 16
    largest = i # Start by assuming the largest is the current index i
    # Check if left child exists and is greater than the current largest
    if left < heap_size and A[left] > A[largest]:
        largest = left  
    # Check if right child exists and is greater than the current largest
    if right < heap_size and A[right] > A[largest]:
        largest = right 
    # If the largest is not the current index i, swap and continue heapifying
    if largest != i:
        A[i], A[largest] = A[largest], A[i] # Swap elements
        max_heapify(A, heap_size, largest) # Recursively heapify the affected subtree

def build_heap(A):
    heap_size = len(A)  # Get the size of the array
    # Start from the last non-leaf node and heapify each node
    for i in range((heap_size//2) - 1, -1, -1): # change range to start index (heap_size//2)-1
        max_heapify(A, heap_size, i) # line 29

def heapsort(A):
    heap_size = len(A)  # Get the size of the array
    build_heap(A) # line 33 - Build the max heap from the array
    #print(A) # Show the max heap structure
    # Perform the heapsort by repeatedly removing the largest element
    for i in range(heap_size - 1, 0, -1):
        A[0], A[i] = A[i], A[0]  # Swap the root (largest) with the last element
        heap_size -= 1  # Reduce the heap size
        max_heapify(A, heap_size, 0)  # Restore the max heap property

# A = [8, 3, 1, 7, 0, 10, 2, 5, 4, 9, 6]
# heapsort(A)
# print(A) 