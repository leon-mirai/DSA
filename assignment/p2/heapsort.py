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

def Heapsort(arr):
    build_max_heap(arr)
    # swap greatest parent with smallest child
    # delete greatest parent
    heapify(arr, 1)

def build_max_heap(arr):
    heap_size = len(arr)
    for i in range(heap_size / 2, -1, -1):
        heapify(arr, heap_size, i)

def heapify(arr, heap_size, index):
    left = 2 * index + 1
    right = 2 * index + 1
    largest = index
    if left < heap_size and arr[left] > arr[largest]:
        largest = right
    
    return
    
    

arr = [2, 8, 5, 3, 9, 1]