def find_max(arr): 
    max_value = arr[0] # 2
    for num in arr: # 1 for each loop
        if num > max_value: # 2 for each loop
            max_value = num # 1 for each loop
    return max_value # 1


"""
T(n) = 3n + 3
Big-O notation is therefore O(n)
"""