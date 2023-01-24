# import networkx as nx

# def iddfs(graph, start, goal):
#     for depth in range(0, len(graph)):
#         path = dls(graph, start, goal, depth)
#         if path is not None:
#             return path
#     return None

# def dls(graph, start, goal, depth):
#     if start == goal:
#         return [start]
#     if depth <= 0:
#         return None
#     for next_node in graph[start]:
#         path = dls(graph, next_node, goal, depth-1)
#         if path is not None:
#             return [start] + path
#     return None

# G = nx.Graph()
# G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)])
# path = iddfs(G, 1, 7)
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
    "C": ['G'],
    'D': [],
    'E': ['F'],
    'G': [],
    'F': []
}

path = list()


def DFS(currentNode, destination, graph, maxDepth, curList):
    print("Checking for destination", currentNode)
    curList.append(currentNode)
    if currentNode == destination:
        return True
    if maxDepth <= 0:
        path.append(curList)
        return False
    for node in graph[currentNode]:
        if DFS(node, destination, graph, maxDepth-1, curList):
            return True
        else:
            curList.pop()
    return False


def iterativeDDFS(currentNode, destination, graph, maxDepth):
    for i in range(maxDepth):
        curList = list()
        if DFS(currentNode, destination, graph, i, curList):
            return True
    return False


if not iterativeDDFS('A', 'E', graph, 4):
    print("Path is not available")
else:
    print("A path exists")
    print(path.pop())
