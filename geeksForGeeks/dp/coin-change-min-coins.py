
# recursive - self made - didn't check
def helper(arr, count, value):
    
    if not value:
        return 0
    if count == -1:
        return float('inf')
    
    res = helper(arr, count - 1, value)
    if arr[count] <= value:
        res = min(res, 1 + helper(arr, count, value - arr[count]))
        
    return res


# dp - 2d - self made - didn't check
def minimumNumberOfCoins(coins, count, value):

    dp = [ [0] * (value + 1) ] * (count + 1)
    
    for i in range(count + 1):
        dp[i][0] = 0
    for i in range(1, value + 1):
        dp[0][i] = float('inf')
    
    for i in range(1, count + 1):
        for j in range(1, value + 1):
            dp[i][j] = dp[i - 1][j]
            if coins[i - 1] <= j:
                dp[i][j] = min( dp[i][j], dp[i][j - coins[i]] )
    
    if dp[count][value] == float('inf'):
        return -1
    return dp[count][value]


# dp - 1d 
def minimumNumberOfCoins(coins, count, value):

    dp = [float('inf')] * (value + 1)
    dp[0] = 0
    
    for coin in coins:
        for i in range(1, value + 1):
            if coin <= i:
                dp[i] = min(dp[i], 1 + dp[i - coin])
    
    if dp[value] == float('inf'):
        return -1
    return dp[value]

