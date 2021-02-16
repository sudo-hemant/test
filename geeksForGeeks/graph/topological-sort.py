
# NOTE: pepcoding has explained it very well, why we can't do it directly 
# insted of using stack and again reversing  


# recursive dfs & stack
def topoSort(n, adj):

    is_visited = [False] * n
    res = [] * n
    
    for vertice in range(n):
        if not is_visited[vertice]:
            dfs(vertice, is_visited, res, adj)
    
    # res.reverse()
    return res[::-1]
    
    
def dfs(vertice, is_visited, res, adj):
    is_visited[vertice] = True
    
    for edge in adj[vertice]:
        if not is_visited[edge]:
            dfs(edge, is_visited, res, adj)

    res.append(vertice)
