def bubble_sort(A):
    for i in range(len(A)):
        for j in range(len(A) - 1 - i):
            if A[j] > A[j + 1]:
                swap(A, j, j + 1)

def selection_sort(A):
    n = len(A)
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if A[j] < A[min]:
                min = j
        swap(A, i, min)

def insertion_sort(A):
    n = len(A)
    end = A[0]
    idx = 1
    while idx < n:
        if A[idx] < end:
            x = A.pop(idx)
            for j in range(0, idx):
                if x < A[j]:
                    A.insert(j, x)
                    break
        end = A[idx]
        idx += 1
def swap(A, item1, item2):
    A[item1], A[item2] = A[item2], A[item1]
    
def quick_sort(A, left, right):
    if left < right:
        idx = partition(A, left, right)
        
        quick_sort(A, left, idx - 1)
        quick_sort(A, idx + 1, right)
    
def partition(A, left, right):
    pivot = A[right]
    max_idx = left

    for i in range(left, right):
        if A[i] < pivot:
            swap(A, i, max_idx)
            max_idx += 1
    
        
def heap_sort(A):
    n = len(A)
    if n <= 1:
        return A
    build_heap(A)
    
    for i in range(n - 1, 0, -1):
        swap(A, 0, i)
        n -= 1
        heapify(A, n, 0)

def build_heap(A):
    n = len(A)
    for i in range(n // 2 - 1, -1, -1):
        heapify(A, n, i)
    

def heapify(A, heap_size, idx):
    left = 2 * idx + 1
    right = 2 * idx + 2
    max_idx = idx
    
    if left < heap_size and A[left] > A[max_idx]:
        max_idx = left
    if right < heap_size and A[right] > A[max_idx]:
        max_idx = right
    if max_idx != idx:
        swap(A, max_idx, idx)
        heapify(A, heap_size, max_idx)
    return idx

A = [8, 3, 1, 7, 0, 10, 2, 5, 4, 9, 6]

heap_sort(A)
print(A)

