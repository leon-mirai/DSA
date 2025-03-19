def sum_loop(n):
    total = 0 # O(1)
    for i in range(1, n + 1): # O(n)
        total += i # O(n)
    return total # O(1)
# T(n) = 2n + 2
def sum_formula(n):
    return (n * (n + 1)) // 2 # 3 x O(1)
# 3

"""
Therefore sum_formula is faster than sum_loop as it runs in constant time O(1) compared to
sum_loop which runs in linear-time O(n).

"""
