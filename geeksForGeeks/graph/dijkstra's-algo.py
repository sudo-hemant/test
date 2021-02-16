

# didn't make myself



def dijkstra(src, V, g):

    distance = [float('inf')] * V
    distance[src] = 0
    sptset = [False] * V
    
    for i in range(V):
        u = min_distance(distance, sptset, V)
        sptset[u] = True
        
        for v in range(V):
            if g[u][v] > 0 and not sptset[v] and distance[v] > distance[u] + g[u][v]:
                distance[v] = distance[u] + g[u][v]
    
    return distance
        

def min_distance(distance, sptset, V):
    minn = float('inf')
    
    for vertice in range(V):
        if distance[vertice] < minn and not sptset[vertice]:
            minn = distance[vertice]
            min_index = vertice
            
    return min_index
