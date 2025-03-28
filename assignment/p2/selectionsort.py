def selection_sort(array):
    for i in range(len(array)):
        min = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min]:
                min = j
        array[i], array[min] = array[min], array[i]

my_arr = [3, 6, 2, 1, 9, -3, 6]
selection_sort(my_arr)
print(my_arr)