def heap_sort(A):
    heap_size = len(A)
    if heap_size <= 1:
        return A
    
    build_heap(A)
    
    for i in range(heap_size - 1, 0, - 1):
        A[i], A[0] = A[0], A[i] # swap top most with unsorted 
        heap_size -= 1
        heapify(A, heap_size, 0)
    
def build_heap(A):
    heap_size = len(A)
    
    for i in range(heap_size // 2 - 1, -1, -1):
        heapify(A, heap_size, i)
    
    
def heapify(A, heap_size, i):
    left = 2 * i + 1
    right = 2 * i + 2
    max_idx = i
    
    if left < heap_size and A[left] > A[max_idx]:
        max_idx = left
    if right < heap_size and A[right] > A[max_idx]:
        max_idx = right
    if max_idx != i:
        A[max_idx], A[i] = A[i], A[max_idx]
        

A = [2, 8, 1, 4, 14, 7, 16, 10, 9, 3]
heap_sort(A)
print(A)