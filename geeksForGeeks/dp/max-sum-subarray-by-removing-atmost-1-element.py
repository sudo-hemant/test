
# using kadane's algorithm 

# by using 2 arrays whose value is determined by traversing the array 
# one forward and one backward - using kadanes algo and then again
# traversing the array by considering all elements one by one if we get 
# max subarray by removing that element or not

def maxSumSubarray(arr, n):
    
    if n == 1:
        return arr[0]
    
    forward_arr, backward_arr = [0] * n, [0] * n
    res = arr[0]
    
    forward_arr[0], backward_arr[-1] = arr[0], arr[-1]

    for i in range(1, n):
        forward_arr[i] = max(arr[i], arr[i] + forward_arr[i - 1])
        res = max(res, forward_arr[i])
    
    for i in reversed(range(n - 1)):
        backward_arr[i] = max(arr[i], arr[i] + backward_arr[i + 1])
        res = max(res, backward_arr[i])
        
    for i in range(1, n - 1):
        res = max(res, forward_arr[i - 1] + backward_arr[i + 1])
    
    return res
