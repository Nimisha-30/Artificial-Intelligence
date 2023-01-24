# import networkx as nx

# def depth_limited_search(graph, start, goal, limit):
#     if start == goal:
#         return [start]
#     if limit <= 0:
#         return None
#     for next_node in graph[start]:
#         path = depth_limited_search(graph, next_node, goal, limit-1)
#         if path is not None:
#             return [start] + path
#     return None

# G = nx.Graph()
# G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)])
# path = depth_limited_search(G, 2, 7, 3)
# print(path)

# # Visualization of the path
# pos = nx.spring_layout(G)
# nx.draw(G, pos, with_labels=True)
# path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
# path_nodes = path
# nx.draw_networkx_nodes(G, pos, nodelist=path_nodes, node_color='r')
# nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O'],
    'H': [],
    'I': [],
    'J': [],
    'K': [],
    'L': [],
    'M': [],
    'N': [],
    'O': []
}


def DLS(start, goal, path, level, maxD):
    print('\nCurrent level-->', level)
    print('Goal node testing for', start)
    path.append(start)
    if start == goal:
        print("Goal test successful")
        return path
    print('Goal node testing failed')
    if level == maxD:
        return False
    print('\nExpanding the current node', start)
    for child in graph[start]:
        if DLS(child, goal, path, level+1, maxD):
            return path
        path.pop()
    return False


start = 'A'
goal = input('Enter the goal node:-')
maxD = int(input("Enter the maximum depth limit:-"))
print()
path = list()
res = DLS(start, goal, path, 0, maxD)
if(res):
    print("Path to goal node available")
    print("Path", path)
else:
    print("No path available for the goal node in given depth limit")
