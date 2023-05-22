n=int(input("Enter the number of nodes: "))
l={}
root=0
for i in range(n):
	if(i==0):
		root=input("Enter the root node : ")
		l[root]=[]
		m=int(input("Enter the number of children :"))
		for j in range(m):
			print("Enter the children",j+1,":")
			a=input()
			l[root].append(a)
	else:
		x=input("Enter the another node : ")
		l[x]=[]
		m=int(input("Enter the number of children :"))
		for j in range(m):
			print("Enter the children",j+1,":")
			a=input()
			l[x].append(a)
print(l)
	
	
visited = [] 
queue = [] 

def bfs(visited, graph, node):
	visited.append(node)
	queue.append(node)
	while queue:      
		m = queue.pop(0) 
		print (m, end = " ") 

		for neighbour in graph[m]:
			if neighbour not in visited:
				visited.append(neighbour)
				queue.append(neighbour)
    
print("Breadth First Search :")
bfs(visited, l, root) 

	
visited = set()

def dfs(visited, graph, node):
	if node not in visited:
		print (node, end=" ")
		visited.add(node)
		for neighbour in graph[node]:
			dfs(visited, graph, neighbour)
print("\nDepth First Search :")
dfs(visited, l, root)

   
