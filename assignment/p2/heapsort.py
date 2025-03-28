"""
heap: ordered binary tree
max heap: parent > child
Make tree from array
build-max-heap: create max heap from unsorted array
- swap largest parent with smallest child
- remove largest parent
- now we have a tree again
heapify: similar to build-max-heap, but assumes part of array is already sorted
- call heapify to turn tree into heap
- the smallest child that is at the top now floats down to the bottom 
"""

def heap_sort(A):
    heap_size = len(A)
    if heap_size <= 1:
        return A
    
    build_heap(A) # make max heap
    # repeatedly rebuild heap
    for i in range(heap_size - 1, 0, -1):
        # swap
        A[0], A[i] = A[i], A[0]
        # decrement
        heap_size -= 1
        # heapify
        
    

def build_heap(A):
    return

def heapify(A, heap_size, i):
    return



A = [2, 8, 1, 4, 14, 7, 16, 10, 9, 3]  # Input array
heap_sort(A) # line 42 - Call heapsort to sort the array
print(A)  # Print the sorted array
# def max_heapify(A, heap_size, i):
#     # Calculate left and right child indices
#     left = 2 * i + 1 # line 15
#     right = 2 * i + 2 # line 16
#     largest = i # Start by assuming the largest is the current index i
#     # Check if left child exists and is greater than the current largest
#     if left < heap_size and A[left] > A[largest]:
#         largest = left  
#     # Check if right child exists and is greater than the current largest
#     if right < heap_size and A[right] > A[largest]:
#         largest = right 
#     # If the largest is not the current index i, swap and continue heapifying
#     if largest != i:
#         A[i], A[largest] = A[largest], A[i] # Swap elements
#         max_heapify(A, heap_size, largest) # Recursively heapify the affected subtree

# def build_heap(A):
#     heap_size = len(A)  # Get the size of the array
#     # Start from the last non-leaf node and heapify each node
#     for i in range((heap_size//2) - 1, -1, -1): # change range to start index (heap_size//2)-1
#         max_heapify(A, heap_size, i) # line 29

# def heapsort(A):
#     heap_size = len(A)  # Get the size of the array
#     build_heap(A) # line 33 - Build the max heap from the array
#     print(A) # Show the max heap structure
#     # Perform the heapsort by repeatedly removing the largest element
#     for i in range(heap_size - 1, 0, -1):
#         A[0], A[i] = A[i], A[0]  # Swap the root (largest) with the last element
#         heap_size -= 1  # Reduce the heap size
#         max_heapify(A, heap_size, 0)  # Restore the max heap property

