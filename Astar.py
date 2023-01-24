import networkx as nx
import heapq


def astar(graph, start, goal, heuristic):
    heap = [(0, start, [])]
    visited = set()
    while heap:
        (f, vertex, path) = heapq.heappop(heap)
        if vertex in visited:
            continue
        visited.add(vertex)
        path = path + [vertex]
        if vertex == goal:
            return path
        for neighbor in graph[vertex]:
            g = len(path)
            h = heuristic(neighbor, goal)
            f = g + h
            heapq.heappush(heap, (f, neighbor, path))
    return None


def manhattan_distance(a, b):
    x1, y1 = a, a
    x2, y2 = b, b
    return abs(x1 - x2) + abs(y1 - y2)


G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)])
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)

path = astar(G, 1, 7, manhattan_distance)
print(path)

# Visualization of the path
path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
path_nodes = path
nx.draw_networkx_nodes(G, pos, nodelist=path_nodes, node_color='r')
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)
