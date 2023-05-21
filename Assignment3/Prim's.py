def prim(graph, start):
    mst = []  # minimum spanning tree
    visited = set([start])
    edges = [
        (cost, start, to)
        for to, cost in graph[start].items()
    ]
    edges.sort()

    while edges:
        cost, frm, to = edges.pop(0)
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, cost))
            for to_next, cost in graph[to].items():
                if to_next not in visited:
                    edges.append((cost, to, to_next))
            edges.sort()

    return mst

g = {
    'A': {'B': 9, 'C':75},
    'B': {'A': 9, 'C': 95, 'D': 19, 'E': 42},
    'C': {'A': 75, 'B': 95, 'D': 51, 'E': 66},
    'D': {'B': 19, 'C': 51, 'E': 31},
    'E': {'B': 42, 'C': 66, 'D': 31}
}

# For user input Graph
# graph={}
# nodes=list(map(str,input("Enter the nodes in the graph separated by space :").split(" ")))
# edgwt=[[x,y] for x,y in zip(map(str,input("Enter the edges separated by space : ").split(" ")), map(int,input("Enter their respective weights separated by space : ").split(" ")))]
# for i in nodes:
#     graph[i]={}
#     for j in edgwt:
#         if(j[0][0]==i):
#             graph[i][j[0][1]]=j[1]
#         if(j[0][1]==i):
#             graph[i][j[0][0]]=j[1]

print(prim(g,'A'))
