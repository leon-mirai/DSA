import random
"""
Choose pivot
leftItem > pivot
rightItem < pivot
swap left and right
if right > left:
    stop
    swap leftItem with pivot
"""

def quick_sort(arr, left, right):
    if left < right:
        idx = partition(arr, left, right)
        
        quick_sort(arr, left, idx - 1)
        quick_sort(arr, idx + 1, right)
    
    return arr
    
def partition(arr, left, right):
    pivot = arr[right]
    idx = left
    
    for i in range(left, right):
        if arr[i] < pivot:
            arr[i], arr[idx] = arr[idx], arr[i]
            idx += 1
    arr[right], arr[idx] = arr[idx], arr[right]
    return idx
    
my_array = [8, 7, 6, 4, 5]
quick_sort(my_array, 0, len(my_array) - 1)
print(my_array)

