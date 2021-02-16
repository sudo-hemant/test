


# iterative depth first search
def findIslands(A, N, M):
    
    islands = 0
    stack = []
    # this is direction constant, which ll help us to evaluate whether the given 
    # index of matrix is valid or not 
    # Also this is very important concept to be remembered 
    directions = [-1, 0, 1]  # IMPORTANT
    
    for i in range(N):
        for j in range(M):
            if A[i][j] == 1:
                islands += 1
                stack.append((i, j))
    
                while stack:
                    x, y = stack.pop()
                    A[x][y] = -1
                    
                    for index_x in directions:
                        for index_y in directions:
                            # very important concept, remember this
                            if is_valid(x + index_x, y + index_y, N, M) and A[x + index_x][y + index_y] == 1:
                                stack.append((x + index_x, y + index_y))
                    
    return islands                
    
# to check whether the given index is valid or not
def is_valid(i, j, n, m):
    if i < n and j < m and i > -1 and j > -1:
        return True
    return False
