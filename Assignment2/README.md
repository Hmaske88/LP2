Enter the nodes in the graph separated by space :A B C D E G
['A', 'B', 'C', 'D', 'E', 'G']
Enter the edges in the graph separated by space :AB AE BC ED DG BG
['AB', 'AE', 'BC', 'ED', 'DG', 'BG']
Enter the weight of edge AB : 
2
Enter the weight of edge AE : 
3
Enter the weight of edge BC : 
1
Enter the weight of edge BG : 
9
Enter the weight of edge DG : 
1
Enter the weight of edge ED : 
6
{'A': {'B': 2, 'E': 3}, 'B': {'C': 1, 'G': 9}, 'C': {}, 'D': {'G': 1}, 'E': {'D': 6}, 'G': {}}
Enter heuristic value of A : 
11
Enter heuristic value of B : 
6
Enter heuristic value of C : 
99
Enter heuristic value of D : 
1
Enter heuristic value of E : 
7
Enter heuristic value of G : 
0

Path found :  ['A', 'E', 'D', 'G']
