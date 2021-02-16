


# rec sol

# DID NOT UNDERSTANT


# dp sol
def countWays(m):
    mod = 1000000007
    
    dp = [0] * (m + 1)
    dp[0] = dp[1] = 1
    
    for i in range(2, m + 1):
        dp[i] = (dp[i - 2] % mod + 1) % mod
    
    return dp[m]
