
def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - 1):
            if arr[j] >= arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
def selectionSort(arr):
    for i in range(len(arr)):
        min_pos = i
        for j in range(i + 1, len(arr)):
            if (arr[j] < arr[min_pos]):
                min_pos = j
        arr[min_pos], arr[i] = arr[i], arr[min_pos]

def insertionSort(arr):
    i = 1
    end_of_sorted = arr[0]
    length = len(arr)
    while i < length:
        if arr[i] < end_of_sorted:
            x = arr.pop(i)
            for j in range(0, i):
                if x < arr[j]:
                    arr.insert(j, x)
                    break
        end_of_sorted = arr[i]
        i += 1

array = [3, 1, 4, 1, 5, 9]
insertionSort(array)
print(array)