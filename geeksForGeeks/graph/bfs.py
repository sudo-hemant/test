
# disjoint graph is not considered

# iterative sol 
from collections import deque

def bfs(adj, v):

    is_discovered = [False] * v
    q = deque()
    res = []
    
    q.append(0)
    
    while q:
        popped = q.popleft()
        res.append(popped)
        is_discovered[popped] = True
    
        for edge in adj[popped]:
            if not is_discovered[edge]:
                q.append(edge)
                # making true bcos it might happened that the vertice is in queue 
                # and we might discover it another time and append it again, 
                # so to avoid this kind of situation
                is_discovered[edge] = True

    return res     
