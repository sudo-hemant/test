

# similar to no_of_islands problem

# iterative bfs
from collections import deque

def findMaxArea(n, m, A):
    
    largest_area = 0
    
    for i in range(n):
        for j in range(m):
            if A[i][j]:
                A[i][j] = 0
                largest_area = bfs(i, j, n, m, A, largest_area)
    
    return largest_area
    
    
def bfs(i, j, n, m, A, largest_area):
    q = deque()
    count = 0
    directions = [-1, 0, 1]
    q.append((i, j))
    
    while q:
        x, y = q.popleft()
        count += 1
        
        for index_x in directions:
            for index_y in directions:
                
                if is_valid(x + index_x, y + index_y, n, m) and A[x + index_x][y + index_y]:
                    A[x + index_x][y + index_y] = 0
                    q.append((x + index_x, y + index_y))
                    
    return max(largest_area, count)
                
                
def is_valid(x, y, n, m):
    if x < n and y < m and x >= 0 and y >= 0:
        return True
    return False
