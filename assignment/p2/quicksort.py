def swap(A, item1, item2):
    A[item1], A[item2] = A[item2], A[item1]

# def quick_sort(arr, left, right):
#     if left < right:  # exit when left is after right
#         # Get partition index, which will be used to divide the array
#         idx = partition(arr, left, right)
        
#         # Recursively sort the subarrays
#         quick_sort(arr, left, idx - 1)  # Sort left of pivot
#         quick_sort(arr, idx + 1, right)  # Sort right of pivot
    
#     return arr

def quick_sort(arr):
    # Create an explicit stack
    stack = [(0, len(arr) - 1)]  # Push initial bounds (start, end) to the stack

    while stack:
        # Pop the bounds of the current subarray
        start, end = stack.pop()

        # Perform partitioning
        if start < end:
            pivot_index = partition(arr, start, end)

            # Push the subarrays to the stack, excluding the pivot
            stack.append((start, pivot_index - 1))  # Left subarray
            stack.append((pivot_index + 1, end))    # Right subarray

    return arr

def partition(arr, left, right):
    pivot = arr[right]  # pivot is selected as last index
    idx = left  # idx that finds correct position for pivot
    
    for i in range(left, right):
        if arr[i] < pivot:
            swap(arr, i, idx)
            idx += 1
    
    # Swap the pivot element with the element at idx to place it in the correct position
    swap(arr, right, idx)
    return idx

# # Test the function
# my_array = [8, 3, 1, 7, 0, 10, 2, 5, 4, 9, 6]
# quick_sort(my_array, 0, len(my_array) - 1)
# print(my_array)  # It should print the sorted array
