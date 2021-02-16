import atexit
import io
import sys

# finding the factorial of n and then using formula 
# TC : O(N) AND SC : O(N)

def nCr(n, r): 
    
    if r > n:
        return 0
    
    mod = 1000000007
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] * i 
        
    ans = dp[n] // (dp[r] * dp[n - r])
    
    return ans % mod


#Contributed by : Nagendra Jha


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,r = map(int,input().strip().split())
        print(nCr(n,r))