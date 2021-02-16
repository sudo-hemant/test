

# iterative bfs 
from collections import deque

def rotOranges(mat,r,c):

    time = 0
    q = deque()
    
    for i in range(r):
        for j in range(c):
            if mat[i][j] == 2:
                mat[i][j] = 0
                q.append((i, j))
                
    time = bfs(q, r, c, mat)
    
    for i in range(r):
        for j in range(c):
            if mat[i][j] == 1:
                return -1
                
    return time - 1
    
    
def bfs(q, r, c, mat):
    time = 0
    
    while q:
        length = len(q)
        time += 1
        
        for i in range(length):
            x, y = q.popleft()
            
            if is_valid(x, y - 1, r, c) and mat[x][y - 1] == 1:
                mat[x][y - 1] = 0
                q.append((x, y - 1))
            
            if is_valid(x, y + 1, r, c) and mat[x][y + 1] == 1:
                mat[x][y + 1] = 0
                q.append((x, y + 1))
                
            if is_valid(x - 1, y, r, c) and mat[x - 1][y] == 1:
                mat[x - 1][y] = 0
                q.append((x - 1, y))
                
            if is_valid(x + 1, y, r, c) and mat[x + 1][y] == 1:
                mat[x + 1][y] = 0
                q.append((x + 1, y))
                
    return time
            
            
def is_valid(x, y, r, c):
    if x < r and y < c and x >= 0 and y >= 0:
        return True
    return False
