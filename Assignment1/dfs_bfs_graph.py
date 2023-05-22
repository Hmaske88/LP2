def dfs(visited,graph,node):
    if node not in visited:
        print(node,end = " ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

def bfs(visited,graph,node,queue):
    visited.add(node)
    queue.append(node)
    while queue:
        s = queue.pop(0)
        print(s,end = " ")
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

graph={}
nodes=list(map(str,input("Enter the nodes in the graph separated by space :").split(" ")))
edges=list(map(str,input("Enter the edges in the graph separated by space :").split(" ")))
for i in nodes:
    graph[i]=[]
    for j in edges:
        if(j[0]==i):
            graph[i].append(j[1])
        if(j[1]==i):
            graph[i].append(j[0])
print(graph)
# graph={'A': ['B', 'E'], 'B': ['A', 'C', 'G'], 'C': ['B'], 'D': ['E', 'G'], 'E': ['A', 'D'], 'G': ['D', 'B']}

visited1 = set() # TO keep track of DFS visited nodes
visited2 = set() # TO keep track of BFS visited nodes
queue = []       # For BFS

print("The following is DFS")
dfs(visited1, graph, 'A')

print("\nThe following is BFS")
bfs(visited2, graph, 'A', queue)

