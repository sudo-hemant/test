

# disjoint graph is not considered

# recursive sol
def dfs(adj, vertices):
    
    res = []
    is_visited = [False] * vertices
    helper(adj, 0, is_visited, res)
    
    return res
    

def helper(adj, vertice, is_visited, res):
    res.append(vertice)
    is_visited[vertice] = True
    
    for edge in adj[vertice]:
        if not is_visited[edge]:
            helper(adj, edge, is_visited, res)
