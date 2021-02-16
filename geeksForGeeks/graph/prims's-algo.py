

# didn't make myself

def spanningTree(V, E, graph):
    
    mstSet = [False] * V
    parent = [None] * V
    key = [float('inf')] * V
    
    parent[0] = -1
    key[0] = 0
    
    for vertice in range(V):
        u = min_key(key, mstSet, V, graph)
        mstSet[u] = True
        
        for v in range(V):
            if graph[u][v] > 0 and not mstSet[v] and key[v] > graph[u][v]:
                key[v] = graph[u][v]
                parent[v] = u
    
    return find_cost_mst(parent, V, graph)


def min_key(key, mstSet, V, graph):
    minn = float('inf')
    
    for v in range(V):
        if key[v] < minn and not mstSet[v]:
            minn = key[v]
            min_index = v
            
    return min_index
    
    
def find_cost_mst(parent, V, graph):
    cost = 0
    
    for i in range(1, V):
        cost += graph[i][parent[i]]
    
    return cost
