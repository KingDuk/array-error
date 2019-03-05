from fuzzywuzzy import fuzz
import numpy as np
import random
import time

def mutate(parent):
    x = random.randint(0,len(parent)-1)
    parent[x] = random.randint(0,9)
    print(parent)
    return parent

def gen(cur_gen, pop_size, fittest):
    if cur_gen == 1:
        population = []
        for _ in range(pop_size):
            add_to = []
            for _ in range(6):
                add_to.append(random.randint(0,9))
            population.append(add_to)
        return population
    else:
        population = []
        for _ in range(pop_size):
            print('\n')
            population.append(mutate(fittest))
            print(population)
        return population

def get_fittest(population):
    fitness = []
    for x in population:
        fitness.append(fuzz.ratio(x, [9,9,9,9,9,9]))
    fittest = fitness.index(max(fitness))
    fittest_fitness = fitness[fittest]
    fittest = population[fittest]
    return fittest, fittest_fitness

done = False
generation = 1
population = gen(generation, 10, [0,0,0,0,0,0])
print(population)

while not done:
    generation += 1
    time.sleep(0.5)
    print('Current Generation: ',generation)
    print('Fittest: ',get_fittest(population))
    if get_fittest(population)[1] == 100:
        done = True
    population = gen(generation, 10, get_fittest(population)[0])
    print('Population: ',population)
