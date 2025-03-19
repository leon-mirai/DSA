def countdown(n):
    if n == 0:
        return
    
    print(n)
    
    countdown(n - 1)

countdown(3)

"""
f(3) -> print(3), f(2)
f(2) -> print(2), f(1)
f(1) -> print(1), f(0)
f(0) -> return -> f(1) -> f(2) -> f(3)
complete

"""