import heapq

def dijkstra_mst(graph, start):
    visited = set()
    mst = []
    heap = [(0, start)]
    while heap:
        (cost, node) = heapq.heappop(heap)
        if node not in visited:
            visited.add(node)
            mst.append((cost, node))
            for neighbor, weight in graph[node].items():
                if neighbor not in visited:
                    heapq.heappush(heap, (weight, neighbor))
    return mst

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1},
}
mst = dijkstra_mst(graph, 'A')
print(mst)
