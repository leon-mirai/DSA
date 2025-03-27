import random
"""
Choose pivot
leftItem > pivot
rightItem < pivot
swap left and right
if right > left:
    stop
    swap leftItem with pivot
"""

def quick_sort(arr):
    less = []
    pivot_lst = []
    more = []
    length = len(arr)
    count = 0
    if length <= 1:
        return arr
    else:
        for i in arr:
            my_rand = random.randint(count, length - 1)
            count += 1
            pivot = arr[my_rand]
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivot_lst.append(i)
        less = quick_sort(less)
        more = quick_sort(more)
        print(less + pivot_lst + more)
        return less + pivot_lst + more
            
    

my_array = [8, 2, 1, 3]
quick_sort(my_array)


