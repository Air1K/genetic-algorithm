from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from deap import base, algorithms
from deap import creator
from deap import tools
import random
import numpy as np

app = FastAPI()

# Ваш код с dikstryFitness, cxOrdered, mutShuffleIndexes и т.д.

class InputData(BaseModel):
    matrix: list
    start: int

class OutputData(BaseModel):
    result: list
    logs: list
    hall_of_fame: list

@app.post("/run_algorithm", response_model=OutputData)
async def run_algorithm(data: InputData):
    D = data.matrix
    startV = data.start

    LENGTH_D = len(D)
    LENGTH_CHROM = len(D) * len(D[0])   # длина хромосомы, подлежащей оптимизации

    # константы генетического алгоритма
    POPULATION_SIZE = 500   # количество индивидуумов в популяции
    P_CROSSOVER = 0.9       # вероятность скрещивания
    P_MUTATION = 0.1        # вероятность мутации индивидуума
    MAX_GENERATIONS = 30    # максимальное количество поколений
    HALL_OF_FAME_SIZE = 1

    hof = tools.HallOfFame(HALL_OF_FAME_SIZE)

    RANDOM_SEED = 42
    random.seed(RANDOM_SEED)

    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMin)

    toolbox = base.Toolbox()
    toolbox.register("randomOrder", random.sample, range(LENGTH_D), LENGTH_D)
    toolbox.register("individualCreator", tools.initRepeat, creator.Individual, toolbox.randomOrder, LENGTH_D)
    toolbox.register("populationCreator", tools.initRepeat, list, toolbox.individualCreator)

    population = toolbox.populationCreator(n=POPULATION_SIZE)


    def dikstryFitness(individual):
        s = 0
        for n, path in enumerate(individual):
            path = path[:path.index(n)+1]

            si = startV
            for j in path:
                s += D[si][j]
                si = j

        return s,         # кортеж

    def cxOrdered(ind1, ind2):
        for p1, p2 in zip(ind1, ind2):
            tools.cxOrdered(p1, p2)

        return ind1, ind2

    def mutShuffleIndexes(individual, indpb):
        for ind in individual:
            tools.mutShuffleIndexes(ind, indpb)

        return individual,


    toolbox.register("evaluate", dikstryFitness)
    toolbox.register("select", tools.selTournament, tournsize=3)
    toolbox.register("mate", cxOrdered)
    toolbox.register("mutate", mutShuffleIndexes, indpb=1.0/LENGTH_CHROM/10)

    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("min", np.min)
    stats.register("avg", np.mean)

    population, logbook = algorithms.eaSimple(population, toolbox,
                                            cxpb=P_CROSSOVER/LENGTH_D,
                                            mutpb=P_MUTATION/LENGTH_D,
                                            ngen=MAX_GENERATIONS,
                                            halloffame=hof,
                                            stats=stats,
                                            verbose=True)

    maxFitnessValues, meanFitnessValues = logbook.select("min", "avg")

    best = hof.items[0]
    print(best)

    return {'result': best, 'logs': logbook, 'hall_of_fame': hof}