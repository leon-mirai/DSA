def mergeSortedArrays(a, b):
    merged = []
    i = 0
    j = 0
    
    if len(a) == 0 or len(b) == 0:
        return a + b  
    
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            merged.append(a[i])
            i += 1
        elif b[j] <= a[i]:
            merged.append(b[j])
            j += 1

    return merged+a[i:]+b[j:]
        
    
    return merged
        
print(mergeSortedArrays([0, 3, 4, 31], [4, 6, 30]))