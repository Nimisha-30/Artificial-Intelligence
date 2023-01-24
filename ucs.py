# import heapq
# import networkx as nx

# def uniform_cost_search(graph, start, goal):
#     frontier = []
#     heapq.heappush(frontier, (0, start))
#     came_from = {}
#     cost_so_far = {}
#     came_from[start] = None
#     cost_so_far[start] = 0
#     while frontier:
#         current = heapq.heappop(frontier)[1]
#         if current == goal:
#             break
#         for next_node in graph[current].keys():
#             new_cost = cost_so_far[current] + graph[current][next_node]['weight']
#             if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
#                 cost_so_far[next_node] = new_cost
#                 priority = new_cost
#                 heapq.heappush(frontier, (priority, next_node))
#                 came_from[next_node] = current
#     return came_from, cost_so_far

# def construct_path(came_from, start, goal):
#     current = goal
#     path = [current]
#     while current != start:
#         current = came_from[current]
#         path.append(current)
#     path.reverse()
#     return path

# G = nx.Graph()
# G.add_edges_from([(1, 2, {'weight': 2}), (1, 3, {'weight': 1}), (2, 4, {'weight': 3}), (2, 5, {'weight': 4}), (3, 6, {'weight': 2}), (3, 7, {'weight': 2})])
# came_from, cost_so_far = uniform_cost_search(G, 1, 7)
# path = construct_path(came_from, 1, 7)
# print(path)

# # Visualization of the path
# pos = nx.spring_layout(G)
# nx.draw(G, pos, with_labels=True)
# path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
# path_nodes = path
# nx.draw_networkx_nodes(G, pos, nodelist=path_nodes, node_color='r')
# nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)

# Python3 implementation of above approach

# returns the minimum cost in a vector( if
# there are multiple goal states)
def uniform_cost_search(goal, start):

    # minimum cost upto
    # goal state from starting
    global graph, cost
    answer = []

    # create a priority queue
    queue = []

    # set the answer vector to max value
    for i in range(len(goal)):
        answer.append(10**8)

    # insert the starting index
    queue.append([0, start])

    # map to store visited node
    visited = {}

    # count
    count = 0

    # while the queue is not empty
    while (len(queue) > 0):

        # get the top element of the
        queue = sorted(queue)
        p = queue[-1]

        # pop the element
        del queue[-1]

        # get the original value
        p[0] *= -1

        # check if the element is part of
        # the goal list
        if (p[1] in goal):

            # get the position
            index = goal.index(p[1])

            # if a new goal is reached
            if (answer[index] == 10**8):
                count += 1

            # if the cost is less
            if (answer[index] > p[0]):
                answer[index] = p[0]

            # pop the element
            del queue[-1]

            queue = sorted(queue)
            if (count == len(goal)):
                return answer

        # check for the non visited nodes
        # which are adjacent to present node
        if (p[1] not in visited):
            for i in range(len(graph[p[1]])):

                # value is multiplied by -1 so that
                # least priority is at the top
                queue.append(
                    [(p[0] + cost[(p[1], graph[p[1]][i])]) * -1, graph[p[1]][i]])

        # mark as visited
        visited[p[1]] = 1

    return answer


# main function
if __name__ == '__main__':

    # create the graph
    graph, cost = [[] for i in range(8)], {}

    # add edge
    graph[0].append(1)
    graph[0].append(3)
    graph[3].append(1)
    graph[3].append(6)
    graph[3].append(4)
    graph[1].append(6)
    graph[4].append(2)
    graph[4].append(5)
    graph[2].append(1)
    graph[5].append(2)
    graph[5].append(6)
    graph[6].append(4)

    # add the cost
    cost[(0, 1)] = 2
    cost[(0, 3)] = 5
    cost[(1, 6)] = 1
    cost[(3, 1)] = 5
    cost[(3, 6)] = 6
    cost[(3, 4)] = 2
    cost[(2, 1)] = 4
    cost[(4, 2)] = 4
    cost[(4, 5)] = 3
    cost[(5, 2)] = 6
    cost[(5, 6)] = 3
    cost[(6, 4)] = 7

    # goal state
    goal = []

    # set the goal
    # there can be multiple goal states
    goal.append(6)

    # get the answer
    answer = uniform_cost_search(goal, 0)

    # print the answer
    print("Minimum cost from 0 to 6 is = ", answer[0])

# This code is contributed by mohit kumar 29
