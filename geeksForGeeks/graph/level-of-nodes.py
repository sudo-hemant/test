

# iterative bfs

from collections import deque

def levels(adj,n,x):

    is_visited = [False] * n
    q = deque()
    
    q.append((0, 0))

    while q:
        node, level = q.popleft()
        is_visited[node] = True
        if node == x:
            return level
            
        for edge in adj[node]:
            if not is_visited[edge]:
                q.append((edge, level + 1))
                
    return -1
