def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) -1):
            if (arr[j] < arr[j + 1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]


def selectionSort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            if (arr[j] < arr[min]):
                min = j
        arr[i], arr[min] = arr[min], arr[i]

def insertionSort(arr):
    i = 1
    end_of_sorted = arr[0]
    length = len(arr)
    while i < length:
        if (arr[i] < end_of_sorted):
            min = arr.pop(i)
            for j in range(0, i):
                if min < arr[j]:
                    min = j

        end_of_sorted = arr[i]
        i += 1
array = [5,4,2,3,1,9,17,15,13,167]
print(array)
insertionSort(array)
print(array)

