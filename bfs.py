# import networkx as nx

# def bfs(graph, start, goal):
#     queue = [(start, [start])]
#     while queue:
#         (vertex, path) = queue.pop(0)
#         set1=set(graph[vertex])
#         set2=set1-set(path)
#         for next_node in set2:
#             if next_node == goal:
#                 return path + [next_node]
#             else:
#                 queue.append((next_node, path + [next_node]))
#     return None

# G = nx.Graph()
# G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)])
# path = bfs(G, 1, 7)
# print(path)

# # Visualization of the path
# pos = nx.spring_layout(G)
# nx.draw(G, pos, with_labels=True)
# path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
# path_nodes = path
# nx.draw_networkx_nodes(G, pos, nodelist=path_nodes, node_color='r')
# nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)

def BFS(graph, start, dest) -> list():  # Input parameters for this method are
    # 1.Graph in which we're going to search for our destination(dest) node
    # 2.start which is our start node and dest which is our destination node
    queue = list()
    visited = list()
    queue.append(start)
    print('Visited', start)
    result = ["Not reachable", list()]
    while queue:
        node = queue.pop(0)
        visited.append(node)
        if node == dest:
            print('Destination node found', node)
            result[0] = 'Reachable'
            break
        print(node, 'Is not a destination node')
        for child in graph[node]:
            if child not in visited:
                queue.append(child)
    result[1] = visited
    return result


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B', 'E'],
    'E': ['B', 'D'],
    'F': ['C', 'H'],
    'G': ['C'],
    'H': ['F']
}
result = BFS(graph, "A", "C")
print(result[0])
print("Path used to traverse :-", result[1])
