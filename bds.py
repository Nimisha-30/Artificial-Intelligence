import networkx as nx


def bidirectional_search(graph, start, goal):
    queue_start = [(start, [start])]
    queue_goal = [(goal, [goal])]
    while queue_start and queue_goal:
        (vertex_start, path_start) = queue_start.pop(0)
        (vertex_goal, path_goal) = queue_goal.pop(0)

        set1 = set(graph[vertex_start])
        set2 = set1 - set(path_start)

        for next_node in set2:
            if next_node in path_goal:
                path_start.append(next_node)
                path_goal.append(next_node)
                path_goal.reverse()
                return path_start + path_goal[1:]
            else:
                queue_start.append((next_node, path_start + [next_node]))

        set3 = set(graph[vertex_goal])
        set4 = set3-set(path_goal)

        for next_node in set4:
            if next_node in path_start:
                path_start.append(next_node)
                path_goal.append(next_node)
                path_goal.reverse()
                return path_start + path_goal[1:]
            else:
                queue_goal.append((next_node, path_goal + [next_node]))
    return None


G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)])
path = bidirectional_search(G, 1, 7)
print(path)

# Visualization of the path
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
path_nodes = path
nx.draw_networkx_nodes(G, pos, nodelist=path_nodes, node_color='r')
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)
