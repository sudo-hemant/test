
# iterative bfs

from collections import deque
def is_possible(M, N):
    
    for i in range(N):
        for j in range(N):
            if M[i][j] == 1:
                if is_path(i, j, M, N):
                    return 1
                return 0
                

def is_path(i, j, M, N):
    q = deque()
    q.append((i, j))
    
    while q:
        x, y = q.popleft()
        if M[x][y] == 2:
            return True
        M[x][y] = 0
        
        if is_valid(x, y - 1, M, N) and M[x][y - 1] != 0:
            q.append((x, y - 1))
        if is_valid(x, y + 1, M, N) and M[x][y + 1] != 0:
            q.append((x, y + 1))
        if is_valid(x - 1, y, M, N) and M[x - 1][y] != 0:
            q.append((x - 1, y))
        if is_valid(x + 1, y, M, N) and M[x + 1][y] != 0:
            q.append((x + 1, y))
        
    return False
        
        
def is_valid(x, y, M, N):
    if x < N and y < N and x >= 0 and y >= 0:
        return True
    return False
