def insertion_sort(array):
    length = len(array)
    end = array[0]
    i = 1
    
    while i < length:
        if array[i] < end:
            x = array.pop(i)
            for j in range(0, i):
                if x < array[j]:
                    array.insert(j, x)
                    break
        end = array[i]
        i += 1


my_arr = [3, 6, 2, 1, 9, -3, 6]
insertion_sort(my_arr)
print(my_arr)