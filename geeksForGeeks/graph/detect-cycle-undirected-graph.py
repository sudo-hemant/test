



def isCyclic(adj, n):
    
    is_visited = [False] * n
    
    for i in range(n):
        if not is_visited[i]:
            if dfs(i, -1, is_visited, adj):
                return 1
    return 0
    
    
def dfs(node, parent, is_visited, adj):
    is_visited[node] = True
    
    for edge in adj[node]:
        if not is_visited[edge]:
            if dfs(edge, node, is_visited, adj):
                return 1
        # if the node is already visited and it is not parent, then cycle exists
        elif edge != parent:
            return 1
    return 0
