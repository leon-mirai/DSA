def insertion_sort(array):
    length = len(array)
    end = array[0]
    i = 1
    
    while i < length:
        if array[i] < end:
            x = array.pop(i) # pop item
            for j in range(0, i): # divide/conquer left side
                if x < array[j]: 
                    array.insert(j, x) # insert x before idx j
                    break
        end = array[i] # update end
        i += 1 # increment i


my_arr = [3, 6, 2, 1, 9, -3, 6]
insertion_sort(my_arr)
print(my_arr)