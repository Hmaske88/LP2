graph={}

nodes=list(map(str,input("Enter the nodes in the graph separated by space :").split(" ")))
print(nodes)
# nodes=['A', 'B', 'C', 'D', 'E', 'G']

edgwt=[[x,y] for x,y in zip(map(str,input("Enter the edges separated by space : ").split(" ")), map(int,input("Enter their respective weights separated by space : ").split(" ")))]
for i in nodes:
    graph[i]={}
    for j in edgwt:
        if(j[0][0]==i):
            graph[i][j[0][1]]=j[1]
        if(j[0][1]==i):
            graph[i][j[0][0]]=j[1]
print(graph)
# graph={'A': {'B': 2, 'E': 3}, 'B': {'A': 2, 'C': 1, 'G': 9}, 'C': {'B': 1}, 'D': {'E': 6, 'G': 1}, 'E': {'A': 3, 'D': 6}, 'G': {'B': 9, 'D': 1}}

h={}
for i in nodes:
    print("Enter heuristic value of "+ i +" : ")
    h[i]=int(input())
# h={'A': 11, 'B': 6, 'C': 99, 'D': 1, 'E': 7, 'G': 0} 
        
def aStarAlgo(start_node, stop_node):
    open_set=set(start_node)
    close_set=set()
    
    g={}
    parent={}
    
    g[start_node]=0
    parent[start_node]=start_node
    
    while(len(open_set)):
        n=None
        
        for v in open_set:
            if (n==None or (g[v]+h[v] < g[n]+h[n])):
                n=v
        
        if(n==stop_node or graph[n]==None):
            pass
        else:
            for m,weight in graph[n].items():
                if(m not in open_set and m not in close_set):
                    open_set.add(m)
                    parent[m]=n
                    g[m]=g[n]+weight
                else:
                    if(g[m]>g[n]+weight):
                        g[m]=g[n]+weight
                        parent[m]=n
                        if(m in close_set):
                            close_set.remove(m)
                            open_set.add(m)
        
        if(n==None):
            print("Path does not exist")
            return None
        
        if(n==stop_node):
            path=[]
            
            while(parent[n]!=n):
                path.append(n)
                n=parent[n]
                
            path.append(start_node)
            
            path.reverse()
            
            print("\nPath found : ",path)
            return path
            
        open_set.remove(n)
        close_set.add(n)
        
    print("Path does not exist")
    return None
    
aStarAlgo('A','G')
