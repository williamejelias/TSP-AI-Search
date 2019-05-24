import Initialise
import random
import math
import sys


# generate initial random tour to start
def random_tour():
    tour = []
    for i in range(1, (numberOfCities + 1)):
        tour.append(i)
    random.shuffle(tour)
    return tour


# from a tour, randomly swap two cities and output
def random_tour_swap(input_list):
    swap_indices = random.sample(range(numberOfCities), 2)
    index1 = swap_indices[0]
    index2 = swap_indices[1]
    new_list = list(input_list)
    temp = input_list[index1]
    new_list[index1] = new_list[index2]
    new_list[index2] = temp
    return new_list


# calculate length of a tour
def tour_length(tour):
    length = 0
    for i in range(len(tour) - 1):
        length += distanceMatrix[tour[i] - 1][tour[i + 1] - 1]
    length += distanceMatrix[tour[0] - 1][tour[-1] - 1]
    return length




# simulated annealing
def anneal(cities, matrix, temperature, cooling_rate):
    global currentTour
    global lengthOfTour
    currentTour = random_tour()
    while temperature >= 0.0000001:
        temperature /= cooling_rate
        successor = list(random_tour_swap(currentTour))
        delta = tour_length(successor) - tour_length(currentTour)
        if delta <= 0:
            currentTour = list(successor)
        else:
            probability = random.randint(1, 100) / 100
            if probability <= math.e ** (-delta / temperature):
                currentTour = successor
    lengthOfTour = tour_length(currentTour)
    return currentTour


# function to run annealing as many times as the parameter, and return the best tour/length
def find_best(cities, matrix, temperature, cooling_rate, repetition):
    global overallBestTour
    global overallBestFitness
    global currentTour
    global lengthOfTour
    overallBestTour = anneal(cities, matrix, temperature, cooling_rate)
    overallBestFitness = tour_length(overallBestTour)
    print("current best: ", overallBestFitness, "\n", overallBestTour)
    for i in range(repetition):
        print("*: i = ", i)
        new_tour = anneal(cities, matrix, temperature, cooling_rate)
        if tour_length(new_tour) < overallBestFitness:
            print("new best: ", tour_length(new_tour), "\n", new_tour)
            overallBestTour = new_tour
            overallBestFitness = tour_length(overallBestTour)
    return overallBestTour


try:
    filepath = sys.argv[1]
    initialisedList = Initialise.initialise(filepath)
    cityFileName = initialisedList[0]
    numberOfCities = initialisedList[1]
    distanceMatrix = initialisedList[2]
    currentTour = []
    lengthOfTour = 0

    initialTour = random_tour()
    overallBestTour = initialTour
    overallBestFitness = tour_length(initialTour)
    temp = sys.argv[2]
    cooling = sys.argv[3]
    repeats = sys.argv[4]
    try:
        find_best(numberOfCities, distanceMatrix, int(temp), float(cooling), int(repeats))
        print(cityFileName, ",")
        print("TOURSIZE = ", numberOfCities, ",")
        print("LENGTH = ", overallBestFitness, ",")
        print(str(overallBestTour))
    except Exception as msg:
        print(msg)
        print("Incorrect argument format")
        exit()
except Exception as msg:
    print(msg)
    print("Incorrect file format...")
    exit()


