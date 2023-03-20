# MDP

class companyMDP:
    def __init__(self):
        self.N = 4
        self.states = ['PU', 'PF', 'RU', 'RF']
        self.transitions = {('PU', 'S'): {'PU': 1}, ('PU', 'A'): {'PU': 0.5, 'PF': 0.5},
                            ('PF', 'S'): {'PU': 0.5, 'RF': 0.5}, ('PF', 'A'): {'PF': 1},
                            ('RU', 'S'): {'RU': 0.5, 'PU': 0.5}, ('RU', 'A'): {'PU': 0.5, 'PF': 0.5},
                            ('RF', 'S'): {'RF': 0.5, 'RU': 0.5}, ('RF', 'A'): {'PF': 1}}
        self.rewards = {'PU': 0, 'PF': 0, 'RU': 10, 'RF': 10}

    def startState(self):
        return self.states[0]

    def isEnd(self, state):
        return state == self.states[self.N - 1]

    def actionsFrom(self, state):
        return ['S', 'A']

    def succProbReward(self, state, action):
        result = []
        for s_ in self.transitions[(state, action)]:
            result.append(
                (s_, self.transitions[(state, action)][s_], self.rewards[s_]))
        return result

    def discount(self):
        return 0.9

    def getStates(self):
        return self.states

    def getReward(self, state):
        return self.rewards[state]


def valueIteration2(mdp):
    def Q(state, action):
        return sum(prob * U[newState] for newState, prob, reward in mdp.succProbReward(state, action))

    # Initialize the values to zero
    U = {}
    for state in mdp.getStates():
        U[state] = mdp.getReward(state)

    i = 0
    while i < 10:
        i += 1
        newU = {}
        for state in mdp.getStates():
            newU[state] = mdp.getReward(
                state) + mdp.discount() * max(Q(state, action) for action in mdp.actionsFrom(state))

        # Check for convergence
        if max(abs(U[state] - newU[state]) for state in mdp.getStates()) < 1e-5:
            break

        U = newU

        # Policy
        # pi = {}
        # for state in mdp.getStates():
        #     pi[state] = max((Q(state, action), action) for action in mdp.actionsFrom(state))[1]

        # Display
        print('{:2} {:2}'.format('s', 'U(s)'))
        for state in mdp.getStates():
            print('{:2} {:2}'.format(state, U[state]))
        print("\n\n")


company = companyMDP()
valueIteration2(company)
