def selection_sort(array):
    for i in range(len(array)): # outer loop
        min = i # min is i: the next unsorted index
        for j in range(i + 1, len(array)): # inner loop iterate from 1
            if array[j] < array[min]: # update min to known minimum j
                min = j
        array[i], array[min] = array[min], array[i] # swap

my_arr = [3, 6, 2, 1, 9, -3, 6]
selection_sort(my_arr)
print(my_arr)