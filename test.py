











# def findTargetSumWays(nums, S):
    
#     array_sum = get_array_sum(nums)
#     required_sum = (S + array_sum + 1 ) // 2
    
#     target_sum = [[0] * (required_sum + 1) for _ in range(len(nums) + 1)]
    
#     for i in range(len(nums) + 1):
#         target_sum[i][0] = 1
    
#     for i in range(1, len(nums) + 1):
#         for j in range(1, required_sum + 1):
#             target_sum[i][j] = target_sum[i - 1][j]
            
#             if nums[i - 1] <= j:
#                 target_sum[i][j] += target_sum[i - 1][j - nums[i - 1]]
#     print(target_sum)            
#     return target_sum[-1][-1]
    
    
    
    
# def get_array_sum( nums):
#     curr_sum = 0
    
#     for num in nums:
#         curr_sum += num
        
#     return curr_sum



# print( findTargetSumWays( [1], 2 ) )































# from collections import deque

# def canReach(arr, start):

#     q = deque()
#     q.append(start)
#     arr[start] *= -1

#     while q:
#         index = q.popleft()
#         # print(index)
#         if arr[index] == 0:
#             return True
#         forward_possible_move = index - arr[index]
#         backward_possible_move = index + arr[index]
        
#         if forward_possible_move < len(arr) and arr[forward_possible_move] >= 0:
#             q.append(forward_possible_move)
#             arr[forward_possible_move] *= -1
#         if backward_possible_move >= 0 and arr[backward_possible_move] >= 0:
#             q.append(backward_possible_move)
#             arr[backward_possible_move] *= -1
        
#     return False



# if __name__ == '__main__':
#     arr = [0, 1]
    
#     ans = canReach(arr, 1)
#     print(ans)




# # --------------------------------------------------------------------------------------

# # from timeit import timeit
# # from time import time

# # start = time()

# # maximum = max
# # max_till_now = 0
# # for i in range(10 ** 7):
# #     max_till_now = maximum(i, max_till_now)

# # end = time()

# # print(end - start)

# # --------------------------------------------------------------------------------------



