

# kind of fibonacci but with ans as addition of previous 3

# 1-D sol
def countWays(n):
    if n <= 1:
        return 1
    mod = 1000000007
    
    first = second = 1
    third = 2
    
    for i in range(3, n + 1):
        new = (first + second + third ) % mod
        first, second, third = second, third, new
    
    return third % mod
