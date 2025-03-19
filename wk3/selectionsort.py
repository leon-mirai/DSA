arr = [9, 7, 3, 5, 6, 6, 3, 1, 5, 0]

def selectionSort(array):
    for i in range(len(array)):
        min = i # smallest number
        for j in range(i + 1, len(array)):
            if (array[j] < array[i]):
                min = j
        array[i], array[min] = array[min], array[i]

selectionSort(arr)
print(arr)

# Finds the minimum, then loops till end. If no other min, then swap with min with i