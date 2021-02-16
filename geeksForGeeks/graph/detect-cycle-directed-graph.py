


# recursive depth first search
def isCyclic(n, graph):
    
    is_visited = [False] * n
    # maintaining a recursion array, to detect cycle(backward edge) while doing dfs 
    # we come to any of its ancestors, then we can easily say that it contains cycle
    in_recursion = [False] * n
    
    for vertice in range(n):
        if not is_visited[vertice]:
            if detect_cycle_dfs(vertice, is_visited, in_recursion, graph):
                return True
    return False
    
    
def detect_cycle_dfs(vertice, is_visited, in_recursion, graph):
    
    is_visited[vertice] = True
    in_recursion[vertice] = True
    
    for edge in graph[vertice]:
        if not is_visited[edge] and detect_cycle_dfs(edge, is_visited, in_recursion, graph):
            return True
        # if the node is already visited and we find this in our recursion stack which store
        # all the ancestors, if that node is any of ancestor, if yes then we return true
        elif in_recursion[edge]:
            return True
    
    in_recursion[vertice] = False
    return False
