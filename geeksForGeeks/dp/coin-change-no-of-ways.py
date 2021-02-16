
# recursive sol
def min_coins(coins, count, value):
    if value == 0:
        return 1
    if count == 0:
        return 0
    res = min_coins(coins, count - 1, value)
    if coins[count - 1] <= value:
        res += min_coins(coins, count, value - coins[count - 1])
    return res


# dp 2d sol
def numberOfWays(coins, count, value):
    dp = [ [0]*(value + 1) ]*(count + 1)
    for i in range(count + 1):
        dp[i][0] = 1
    
    for i in range(1, count + 1):
        for j in range(1, value + 1):
            dp[i][j] = dp[i - 1][j]
            if coins[i - 1] <= j:
                dp[i][j] += dp[i][j - coins[i - 1]]
    return dp[count][value]


# dp 1d sol
def numberOfWays(coins, count, value):
    dp = [0] * (value + 1)
    dp[0] = 1
    
    for i in range(count):
        for j in range(coins[i], value + 1):
            dp[j] += dp[j - coins[i]]
    return dp[value]