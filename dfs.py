# import networkx as nx

# def dfs(graph, start, goal):
#     stack = [(start, [start])]
#     while stack:
#         (vertex, path) = stack.pop()
#         set1=set(graph[vertex])
#         set2=set1-set(path)
#         for next_node in set2:
#             if next_node == goal:
#                 return path + [next_node]
#             else:
#                 stack.append((next_node, path + [next_node]))
#     return None

# G = nx.Graph()
# G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)])
# path = dfs(G, 5, 3)
# print(path)

# # Visualization of the path
# pos = nx.spring_layout(G)
# nx.draw(G, pos, with_labels=True)
# path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
# path_nodes = path
# nx.draw_networkx_nodes(G, pos, nodelist=path_nodes, node_color='r')
# nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)

def DFS(graph, start, dest):
    stack = list()
    visited = list()
    stack.append(start)
    visited.append(start)
    print('Visited', start)
    result = ["Not reachable", list()]
    while stack:
        node = stack.pop()
        if node == dest:
            print('Destination node found', node)
            result[0] = 'Reachable'
            break
        print(node, 'Is not a destination node')
        for child in graph[node]:
            if child not in visited:
                visited.append(child)
                stack.append(child)
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
result = DFS(graph, "A", "F")
print(result[0])
print("Path used to traverse :-", result[1])
