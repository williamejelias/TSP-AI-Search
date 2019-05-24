import Initialise
import random
import math

filepath = './cityfiles/AISearchfile017.txt'
initialisedList = Initialise.initialise(filepath)
cityFileName = initialisedList[0]
numberOfCities = initialisedList[1]
distanceMatrix = initialisedList[2]
# need to extract number of cities from initialisation

tours = []
currentTour = []
lengthOfTour = 0


# generate initial random tour to start
def random_tour():
    random_tour = []
    for i in range(1, (numberOfCities + 1)):
        random_tour.append(i)
    random.shuffle(random_tour)
    return random_tour


# calculate length of a tour
def tour_length(tour):
    length = 0
    for i in range(len(tour) - 1):
        length += distanceMatrix[tour[i] - 1][tour[i + 1] - 1]
    length += distanceMatrix[tour[0] - 1][tour[-1] - 1]
    return length


# generate an initial population of tours
def initial_population(population_size):
    global tours
    for i in range(population_size):
        tours.append(random_tour())


# use a 'roulette wheel' to pick two parent tours from the population
# the greater the fitness of a tour the greater the probability of the tour becoming a parent
def roulette_wheel():
    global tours
    sum_of_length = 0
    # sum the inverse of the tour length, as a smaller tour length is preferable
    for i in tours:
        sum_of_length += 1 / tour_length(i)
    pick = random.uniform(0, sum_of_length)
    current = 0
    for tour in tours:
        current += 1 / (tour_length(tour))
        if current > pick:
            return tour


# mutate the child by swapping two cities in it tour by a given probability
def mutate_child(child, probability):
    x = random.randint(0, 100) / 100
    if x < probability:
        swap_indices = random.sample(range(numberOfCities), 2)
        index1 = swap_indices[0]
        index2 = swap_indices[1]
        new_child = list(child)
        temp = child[index1]
        new_child[index1] = new_child[index2]
        new_child[index2] = temp
        return new_child
    else:
        return child


# generate a child using two given parent tours from the population
def generate_child(parent_tour1, parent_tour2, mutate_probability, populationSize):
    # randomly generate an index in which to slice and rejoin parents to form 2 new tours (possibly with repetitions
    # etc)
    random_index = math.floor(int(random.uniform(0, numberOfCities)))
    parent1p1 = list(parent_tour1[:random_index])
    parent1p2 = list(parent_tour1[random_index:])
    parent2p1 = list(parent_tour2[:random_index])
    parent2p2 = list(parent_tour2[random_index:])
    child1 = parent1p1 + parent2p2
    child2 = parent2p1 + parent1p2

    # build list of repeated cities in each child
    temp_list = []
    repeated_values_child1 = []
    repeated_values_child2 = []
    for i in child1:
        if i not in temp_list:
            temp_list.append(i)
        else:
            repeated_values_child1.append(i)
    del temp_list[:]
    for i in child2:
        if i not in temp_list:
            temp_list.append(i)
        else:
            repeated_values_child2.append(i)
    del temp_list[:]

    # fix repeats/missing cities in children
    for i in range(numberOfCities):
        if child1[i] not in temp_list:
            temp_list.append(child1[i])
        else:
            child1[i] = repeated_values_child2.pop()
    del temp_list[:]
    for i in range(numberOfCities):
        if child2[i] not in temp_list:
            temp_list.append(child2[i])
        else:
            child2[i] = repeated_values_child1.pop()
    del temp_list[:]

    # find best child
    mutated1 = mutate_child(child1, mutate_probability)
    mutated2 = mutate_child(child2, mutate_probability)
    if tour_length(mutated1) <= tour_length(mutated2):
        best_child = list(mutated1)
    else:
        best_child = list(mutated2)
    return best_child


# genetic algorithm to find optimum tour
def genetic(population_size, mutate_probability, cut_off):
    print("running genetic")
    global tours
    global overallBestFitness
    global overallBestTour
    initial_population(population_size)
    current_best_fitness = tour_length(tours[0]) + 1
    current_best_tour = tours[0]

    cycle = 0
    # while cycle < cut_off:
    while cycle < cut_off:
        # create new population
        new_tours = []
        count = 0
        while count < population_size:
            parent1 = roulette_wheel()
            parent2 = roulette_wheel()
            mutated_child = generate_child(parent1, parent2, mutate_probability, population_size)
            new_tours.append(mutated_child)
            count += 1
        tours = new_tours

        # find the best tour/fitness of the current population
        for tour in tours:
            if tour_length(tour) < current_best_fitness:
                current_best_tour = tour
                current_best_fitness = tour_length(current_best_tour)

        # if overall best tour is not replaced after cut_off times, output the result
        if current_best_fitness >= overallBestFitness:
            # print("no new best. cycle = ", cycle)
            cycle += 1
        if current_best_fitness < overallBestFitness:
            print("new overall best: ", current_best_fitness, "\n", current_best_tour)
            overallBestFitness = current_best_fitness
            overallBestTour = current_best_tour
            cycle = 0
    # print("TOURSIZE = ", bestFitness, ",")
    # print("TOUR = ", bestTour, ",")
    print("exited loop")
    return_list = [overallBestFitness, overallBestTour]
    return return_list


initial_population(10)
overallBestFitness = tour_length(tours[0])
overallBestTour = tours[0]


# repeat the genetic algorithm a number of times and print the best tour/length
def find_best(population_size, mutate_probability, cut_off, repetition):
    pop_list = genetic(population_size, mutate_probability, cut_off)
    best_fitness = pop_list[0]
    best_tour = pop_list[1]
    for i in range(repetition):
        # print("*: i = ", i)
        new_list = genetic(population_size, mutate_probability, cut_off)
        fit = new_list[0]
        tour = new_list[1]
        if fit < best_fitness:
            best_tour = tour
            best_fitness = fit
            print("LENGTH = ", best_fitness, ",")
            print(best_tour, )
    return_list = [best_fitness, best_tour]
    return return_list


print(cityFileName, ",")
print("SIZE = ", numberOfCities, ",")
find_best(100, 0.5, 1000, 10)
