



from collections import deque

def findMother(adj, v):

    is_visited = [False] * v
    last_visited = -1
    count = 0
    
    for vertice in range(v):
        if not is_visited[vertice]:
            # dfs(vertice, is_visited, adj, count)
            count = bfs(vertice, is_visited, adj)
            last_visited = vertice
    
    # for i in range(v):
    #     is_visited[i] = False
    # dfs(last_visited, is_visited, adj, count)

    is_visited = [False] * v    
    bfs(last_visited, is_visited, adj) 
    
    # print(count)
    
    if any(not value for value in is_visited):
        return -1
    return last_visited
            
  
def bfs(vertice, is_visited, adj):
    q = deque()
    q.append(vertice)
    
    while q:
        popped = q.popleft()
        is_visited[popped] = True
        
        for edge in adj[popped]:
            if not is_visited[edge]:
                q.append(edge)
    
            
# def dfs(vertice, is_visited, adj, count):
#     is_visited[vertice] = True
    
#     for edge in adj[vertice]:
#         if not is_visited[edge]:
#             dfs(edge, is_visited, adj, count)
    
