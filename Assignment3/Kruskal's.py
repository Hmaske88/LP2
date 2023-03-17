def kruskal(graph):
    mst = []  # minimum spanning tree
    visited2 = set() # for storing visited elements for cycle checking
    visited=[]
    edges = []
    for node in graph.keys():
        visited.append(node)
        for to, cost in graph[node].items():
            if(to not in visited):
                edges.append((cost, node, to))
    edges.sort()
    
    i=0
    while(i<len(edges)):
        cost, frm, to= edges[i]
        if(frm not in visited2 or to not in visited2): #if one of the node is not in visited2 then they will not form cycle
            mst.append((frm,to,cost))
            visited2.add(frm)
            visited2.add(to)
        i+=1
    return mst

g = {
    'A': {'B': 9, 'C':75},
    'B': {'A': 9, 'C': 95, 'D': 19, 'E': 42},
    'C': {'A': 75, 'B': 95, 'D': 51, 'E': 66},
    'D': {'B': 19, 'C': 51, 'E': 31},
    'E': {'B': 42, 'C': 66, 'D': 31}
}

print(kruskal(g))
