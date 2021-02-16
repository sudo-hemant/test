



# recursive approach
def maximizeTheCuts(n, x, y, z):
    def helper(i, length, arr):
        if not length:
            return 0
        if i < 0:
            return float('-inf')

        # not including the current cut 
        res = helper(i - 1, length, arr)

        # including the current cut
        if arr[i] <= length:
            res = max(res, helper(i, length - arr[i], arr) + 1)

        return res

    arr = [x, y, z]
    helper(2, n, arr)



# 2-d dp approach

def maximizeTheCuts(n, x, y, z):

    # initializing it with -inf instead of - 1 bcos there are cases when the 
    # cut is not possible and we do max(-1, -1 + 1) comparision in which our  
    # op should be -1 but we get 0, so to avoid such blunders
    cache = [ [float('-inf')] * (n + 1) ] * (4)
    possible_cuts = [x, y, z]

    # initializing the length 0 with 0
    for i in range(4):
        cache[i][0] = 0
        
    for i in range(1, 4):
        for j in range(1, n + 1):
            cache[i][j] = cache[i - 1][j]
            
            # when we include the cut 
            if possible_cuts[i - 1] <= j:
                cache[i][j] = max(cache[i][j], 1 + cache[i][j - possible_cuts[i - 1]] )
            
    if cache[-1][-1] == float('-inf'):
        return 0
    return cache[-1][-1]


if __name__ == '__main__':
    t=int(input())
    for tcs in range(t):
        n=int(input())
        x,y,z=[int(x) for x in input().split()]
        
        print(maximizeTheCuts(n,x,y,z))