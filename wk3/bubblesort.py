array = [5, 9, 3, 2, 1, 5, 7]

def bubble_sort(a):
    for i in range(len(a)):
        for j in range(0, len(a) - 1):
            if (a[j] > a[j + 1]):
                a[j], a[j + 1] = a[j+ 1], a[j]
                
print(array)
bubble_sort(array)
print(array)