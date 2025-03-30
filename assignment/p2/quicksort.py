def swap(A, item1, item2):
    A[item1], A[item2] = A[item2], A[item1]

def quick_sort(arr, left, right):
    if left < right: # exit when left is after right
        idx = partition(arr, left, right) # get partition
        
        quick_sort(arr, left, idx - 1)
        quick_sort(arr, idx + 1, right)
    
    return arr
    
def partition(arr, left, right):
    pivot = arr[right] # pivot is selected as last index
    idx = left # idx that finds correct position for pivot
    
    for i in range(left, right):
        print(f"i: arr[{i}] = {arr[i]}")
        if arr[i] < pivot:
            print(f"idx: arr[{idx}] = {arr[idx]}")
            swap(arr, i, idx)
            idx += 1
    swap(arr, right, idx)
    return idx
    
my_array = [8, 3, 1, 7, 0, 10, 2, 5, 4, 9, 6]
quick_sort(my_array, 0, len(my_array) - 1)
print(my_array)

