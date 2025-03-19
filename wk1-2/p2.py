def sum_numbers(n):
    if n == 0:
        return 0
    return n + sum_numbers(n - 1)

print(sum_numbers(3))

"""
f(3) -> 3 + f(3 - 1)
f(2) -> 2 + f(2 - 1)
f(1) -> 1 + f(1 - 1)
f(0) -> return -> f(1) -> f(2) -> f(3)

result = 6

"""