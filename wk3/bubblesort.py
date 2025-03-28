array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

def bubble_sort(a):
    for i in range(len(a)):
        for j in range(0, len(a) - 1):
            if (a[j] > a[j + 1]):
                a[j], a[j + 1] = a[j+ 1], a[j]
                
print(array)
bubble_sort(array)
print(array)