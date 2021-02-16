


# rec sol

#   ASK


# DP SOL
def count(score):
    dp = [0] * (score + 1)
    dp[0] = 1
    
    for i in range(3, score + 1):
        dp[i] += dp[i - 3]
    for i in range(5, score + 1):
        dp[i] += dp[i - 5]
    for i in range(10, score + 1):
        dp[i] += dp[i - 10]

    return dp[score]
