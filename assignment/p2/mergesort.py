def merge_sort(array):
    if len(array) <= 1:
        return array
    else:
        mid = len(array) // 2
        left_arr = array[:mid]
        right_arr = array[mid:]
        return merge(merge_sort(left_arr), merge_sort(right_arr))
    
    
def merge(left, right):
    left_len = len(left)
    right_len = len(right)
    left_index = 0
    right_index = 0
    my_sorted = []

    while (left_index < left_len and right_index < right_len):
        if (left[left_index] < right[right_index]):
            my_sorted.append(left[left_index])
            left_index += 1
        else:
            my_sorted.append(right[right_index])
            right_index += 1
        print(my_sorted + left[left_index:] + right[right_index:])
        return my_sorted + left[left_index:] + right[right_index:]
    
arr = [3, 6, 1, 9, 2]
merge_sort(arr)