"""
1. Understand Problem
2. Plan Approach
- Brute force
- Identify patterns, consrtaints, relationships, paradigms
- Choose data structures
- Outline step in pseudocode
3. Code
- Translate pseudocode
- Modularize code
4. Test cases
- Basic cases
- edge cases
- stress cases
- debug
- validate
5. Analyse and Optimise
- Time
- Space
- Bottlenecks
- Optimise
- Trade-offs



"""

import math
import time
start_time = time.time()



# def totalShares(n):
#     total = 0
#     day = 1
        
#     # accumulate until day-i is a 1-share day
#     while day <= n // 2: 
#         shares = n // day
#         total += shares
#         day += 1
        
#     one_share_days_count = n - n // 2
#     total += one_share_days_count
#     return total
#     # if first 1-share day, then stop.
#     # sum the rest of the 1-share days
    

# def totalShares(n):
#     # n = total number of days
#     # current_share = current number of shares
#     # share_value = value of current_share
#     # final_share = the last share of 1 or more shares with the same value
      
#     total = 0
#     current_share_count = 1
    
#     while (current_share_count <= n):
#         share_value = n // current_share_count
#         final_share = n // share_value
        
#         total += (final_share - current_share_count + 1) * share_value
#         current_share_count = final_share + 1
    
#     return total


# total = 0
# i = 1
# n = 10

# sqrt_n = math.floor(math.sqrt(n))

# for i in range(1, n + 1):
#     x = n // i
#     print(x, end=" ")

# print()


# def totalSharesBrute(n):
#     total = 0
#     for i in range(1, n + 1):
#         total += n // i
#     return total

def total_shares(n):
    total = 0
    sqrt_n = math.floor(math.sqrt(n))
    
    for i in range(1, sqrt_n + 1):
        total += n // i
        
    for j in range(1, n // (sqrt_n + 1) + 1):
        start = n // (j + 1) + 1
        end = n // j
        
        total += j * (start - end + 1)
    return total

print(total_shares(pow(10, 12)))

print("Process finished --- %s seconds ---" % (time.time() - start_time))