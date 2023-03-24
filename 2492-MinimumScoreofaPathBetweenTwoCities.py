# Imports
import heapq 

# Dijkstra’s algorithm
"""Dijkstra’s algorithm is an algorithm for finding the shortest paths between nodes in a graph. 
It works by iteratively selecting the node with the smallest distance from the source node and 
relaxing all of its edges (updating the distances of its neighbors if a shorter path is found). 
The algorithm terminates when all nodes have been visited or when the target node has been reached.

"""

"""
# TimeComplexity: O((E+V)logV), where E is the number of edges and V is the number of vertices (nodes) in the graph. 
# The space complexity is O(V).

def dijkstra(graph, source, target):
    distances = [float('inf')] * len(graph)
    distances[source] = 0
    heap = [(0, source)]
    while heap:
        dist, node = heapq.heappop(heap)
        if dist > distances[node]:
            continue
        for neighbor, weight in graph[node]:
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))
    
    return distances[target]
"""
def dijkstra(n, roads):
    graph = [[] for _ in range(n)]
    for road in roads:
        a, b, distance = road
        print(f'a = {a}, b = {b}, dist ={distance} ')
        graph[a-1].append((b-1, distance))
        print(f'grapha-1={graph[a-1]}')
        graph[b-1].append((a-1, distance))
        print(f'graphb-1={graph[b-1]}')
        print('___________________________________')
    print(f'final_graph = {graph}')
        
    distances = [float('inf')] * n
    distances[0] = 0
    heap = [(0, 0)]

    while heap:
        dist, node = heapq.heappop(heap)
        print(f'dist={dist} and node = {node}, distance = {distances[node]}')
        if dist > distances[node]:
            continue
        for neighbor, weight in graph[node]:
            print(f'neigh : {neighbor}, weight : {weight}, graph[node] {graph[node]}')
            new_dist = dist + weight
            print(f'new_Dist = {new_dist} and dist_neigh : {distances[neighbor]}')
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))
    
    return distances[n-1]

print(dijkstra(roads=[[1,2,9],[2,3,6],[2,4,5],[1,4,7]], n=4))


