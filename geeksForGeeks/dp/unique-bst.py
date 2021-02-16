

# catalan number formula


# done by using formula = C(2n, n) / n + 1
def numTrees(n):

    dp = [0] * (2 * n + 1)
    dp[0] = dp[1] = 1
    
    for i in range(2, 2 * n + 1):
        dp[i] = dp[i - 1] * i
    
    ans = dp[2 * n] // (dp[n] * dp[n + 1])
    mod = 1000000007
    
    return ans % mod
