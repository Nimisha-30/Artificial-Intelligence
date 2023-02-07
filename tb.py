import copy


def getTorchAdj(state, time):
    states = []
    for i in range(8):
        temp = copy.deepcopy(state)
        if temp[0][i] != 0 and i+4 < len(state[0]):
            temp[0][i+4], temp[0][i] = temp[0][i], temp[0][i+4]
            temp[1] += temp[0][i+4]
            if temp[1] < time:
                states.append(temp)

        temp = copy.deepcopy(state)
        if temp[0][i] != 0 and i-4 >= 0:
            temp[0][i-4], temp[0][i] = temp[0][i], temp[0][i-4]
            temp[1] += temp[0][i-4]
            if temp[1] < time:
                states.append(temp)

        temp = copy.deepcopy(state)
        if temp[0][i] != 0 and i < 4:
            for j in range(4):
                temp = copy.deepcopy(state)
                if i != j and state[0][j] != 0:
                    temp[0][j], temp[0][j+4] = temp[0][j+4], temp[0][j]
                    temp[0][i], temp[0][i+4] = temp[0][i+4], temp[0][i]
                    temp[1] += max(temp[0][i+4], temp[0][j+4])
                    if temp[1] < time:
                        states.append(temp)

    return states


def torch(start, end, time):
    queue = [start,]

    while (len(queue) > 0):
        curr = queue.pop(0)
        print(curr)
        if curr[0] == end:
            return True

        adjStates = getTorchAdj(curr, time)

        for i in adjStates:
            queue.append(i)

    return False


initial = [[1, 2, 5, 8, 0, 0, 0, 0], 0]
target = [0, 0, 0, 0, 1, 2, 5, 8]
print(torch(initial, target, 15))
