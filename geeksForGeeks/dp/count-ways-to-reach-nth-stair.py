

# rec sol
def countWays(m):
    if m == 0:
        return 1
    if m < 0:
        return 0
    res = countWays(m - 1)
    res += countWays(m - 2)
    return res






# dp solution
def countWays(m):
    if m <= 1:
        return 1
    first = second = 1
        
    for i in range(2, m + 1):
        first, second = second % 1000000007, (first + second) % 1000000007
        
    return second % 1000000007
