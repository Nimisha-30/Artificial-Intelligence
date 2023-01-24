import networkx as nx


def best_first_search(graph, start, goal, heuristic):
    queue = [(start, [start], 0)]
    while queue:
        (vertex, path, cost) = min(queue, key=lambda x: heuristic(x[0], goal))
        queue.remove((vertex, path, cost))
        for next_node in graph[vertex]:
            if next_node == goal:
                return path + [next_node]
            else:
                new_cost = cost + 1
                queue.append((next_node, path + [next_node], new_cost))
    return None


def manhattan_distance(a, b):
    x1, y1 = a, a
    x2, y2 = b, b
    return abs(x1 - x2) + abs(y1 - y2)


G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)])
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)

path = best_first_search(G, 1, 7, manhattan_distance)
print(path)

# Visualization of the path
path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
path_nodes = path
nx.draw_networkx_nodes(G, pos, nodelist=path_nodes, node_color='r')
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)
