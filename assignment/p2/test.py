def qs(A, left, right):
    if left < right:
        p_idx = partition(A, left, right)
        
        qs(A, left, p_idx - 1)
        qs(A, p_idx + 1, right)
    return A
    
def partition(A, left, right):
    p = A[right]
    p_idx = left
    
    for i in range(left, right):
        if A[i] < p:
            A[i], A[p_idx] = A[p_idx], A[i]
            p_idx += 1
    A[right], A[p_idx] = A[p_idx], A[right]
            
    return p_idx

def hs(A):
    s = len(A)
    if s <= 1:
        return A
    
    bh(A)
    
    for i in range(s - 1, 0, - 1):
        A[0], A[i] = A[i], A[0]
        s -= 1
        h(A, s, 0)
def bh(A):
    s = len(A)
    
    for i in range((s // 2) - 1, -1 , -1):
        h(A, s, i)
def h(A, s, idx):
    l = idx * 2 + 1
    r = idx * 2 + 2
    max_idx = idx
    
    if l < s and A[l] > A[max_idx]:
        max_idx = l
    if r < s and A[r] > A[max_idx]:
        max_idx = r
    if max_idx != idx:
        A[max_idx], A[idx] = A[idx], A[max_idx]
        h(A, s, max_idx)

A = [8, 3, 1, 7, 0, 10, 2, 5, 4, 9, 6]
# qs(A, 0, len(A) - 1)
hs(A)
print(A)

