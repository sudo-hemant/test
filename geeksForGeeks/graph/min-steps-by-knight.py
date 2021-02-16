

# iterative bfs
from collections import deque

def minStepToReachTarget(knightpos, targetpos, N):

    start_x, start_y = knightpos[0] - 1, knightpos[1] - 1
    target_x, target_y = targetpos[0] - 1, targetpos[1] - 1
    
    matrix = [ [1 for j in range(N)] for i in range(N) ]
    
    steps = bfs(start_x, start_y, target_x, target_y, matrix, size)
    return steps
    
    
def bfs(start_x, start_y, target_x, target_y, matrix, size):
    q = deque()
    min_steps = float('inf')
    # to handle the movement of knight
    directions_1 = [-1, 1]
    directions_2 = [-2, 2]
    
    q.append((start_x, start_y, 0))
    matrix[start_x][start_y] = 0
    
    while q:
        a, b, step = q.popleft()
        
        if a == target_x and b == target_y:
            min_steps = min(step, min_steps)
        
        for x in directions_1:
            for y in directions_2:
                
                if is_valid(a + x, b + y, size) and matrix[a + x][b + y]:
                    matrix[a + x][b + y] = 0
                    q.append((a + x, b + y, step + 1))
                
                if is_valid(a + y, b + x, size) and matrix[a + y][b + x]:
                    matrix[a + y][b + x] = 0
                    q.append((a + y, b + x, step + 1))
    
    return min_steps         
       
                
def is_valid(x, y, size):
    if x >= 0 and x < size and y >= 0 and y < size:
        return True
    return False
