def diameter(graph):
    largest = largest_component(graph)
    max_dist = 0

    for v in largest.get_vertices():
        visited, dist,  parent = bfs(largest, v)
        
        local_max = max(d for d in dist.values() if d != float('inf'))  #para cada ponto vê o ponto mais longe de si
        
        max_dist = max(max_dist, local_max) # devolve a dist máxima entre 2 pontos no graph

    return max_dist 
