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

# def heap_sort(A):
#     heap_size = len(A)
#     # if heap size is one returned because it is sorted
#     if heap_size <= 1:
#         return A
#     # Make heap
#     build_heap(A)
    
#     # Loop through nodes e.g. backwards from 9 to 0. 10 in total
#     for node_idx in range(heap_size - 1, 0, -1):
#         A[0], A[node_idx] = A[node_idx], A[0] # swap top node, and last unsorted node
#         heap_size -= 1
#         heapify(A, heap_size, 0) # 
#         # how does 0 input work here?


# def build_heap(A):
#     heap_size = len(A)
    
#     # loop through parent nodes backwards
#     for node_idx in range(heap_size // 2 - 1, -1, -1):
#         heapify(A, heap_size, node_idx) # heapify the nodes

# def heapify(A, heap_size, node_idx):
#     left_node_idx = node_idx * 2 + 1 # left child node
#     right_node_idx = node_idx * 2 + 2 # right child node
#     max_idx = node_idx # index of largest node
    
#     if left_node_idx < heap_size and A[left_node_idx] > A[max_idx]:
#         max_idx = left_node_idx
#     if right_node_idx < heap_size and A[right_node_idx] > A[max_idx]:
#         max_idx = right_node_idx
#     if max_idx != node_idx:
#         A[node_idx], A[max_idx] = A[max_idx], A[node_idx]
# # heapify is the concept of swapping lower position nodes of high value to a higher position to make a heap
# # a heap is esentially a tree that goes down sequentially. min or max heap

A = [8, 3, 1, 7, 0, 10, 2, 5, 4, 9, 6]
heap_sort(A)
print(A) 


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
    print(A) # Show the max heap structure
    # Perform the heapsort by repeatedly removing the largest element
    for i in range(heap_size - 1, 0, -1):
        A[0], A[i] = A[i], A[0]  # Swap the root (largest) with the last element
        heap_size -= 1  # Reduce the heap size
        max_heapify(A, heap_size, 0)  # Restore the max heap property

