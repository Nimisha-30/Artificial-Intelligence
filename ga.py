import random

best = -10000
population = ([[random.randint(0, 1) for x in range(5)] for i in range(4)])
print(type(population))
print(population)
parents = []
newPopulation = []


def fitnessScore():
    global population, best
    fitnessValue = []
    fitnessScore = []
    for i in range(4):
        chromosomeValue = 0
        for j in range(4, 0, -1):
            chromosomeValue += population[i][j]*(2**(5-j))
        chromosomeValue = -1 * \
            chromosomeValue if population[i][0] == 1 else chromosomeValue
        print(chromosomeValue)
        fitnessValue.append(-(chromosomeValue**2)+5)
    print(fitnessValue)
    fitnessValue, population = zip(
        *sorted(zip(fitnessValue, population), reverse=True))
    best = fitnessValue[0]

    def selectParent():
    global parents
    parents = population[0:2]
    print(type(parents))
    print(parents)

    selectParent()

    def crossover():
    global parents
    crossoverPoint = random.randint(0, 4)
    parents = parents + \
        tuple([(parents[0][0:crossoverPoint+1]+parents[1][crossoverPoint+1:5])])
    parents = parents + \
        tuple([(parents[1][0:crossoverPoint+1]+parents[0][crossoverPoint+1:5])])
    print(parents)

    crossover()

    def mutation():
    global population, parents
    mutate = random.randint(0, 49)
    if mutate == 20:
        x = random.randint(0, 3)
        y = random.randint(0, 5)
        parents[x][y] = 1-parents[x][y]
    population = parents
    print(population)

    mutation()

    for i in range(3):
    fitnessScore()
    selectParent()
    crossover()
    mutation()


print(best)
print(population[0])
