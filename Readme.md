# Introduction

Two AI Search algorithms are implemented to try to find optimal solutions to the travelling salesman problem.

Both algorithms take a text file representing distances between cities, and output an array with the order in which cities should be visited to minimise the total tour distance. Due to the nature of the algorithms, the outputs may not always be optimal.

## City File Format

The actual instances of the Travelling Salesman problem (more precisely, the symmetric Travelling Salesman problem, where the distance from city
x to city y, denoted (x, y), is always the same as the distance from city y to city x, that is, (y, x)) will be given in the following form (the cities are
always named 1, 2, ... , n).

* NAME = <string = name-of-the-data-file>
* SIZE = <integer n = the number of cities in the instance>,
* <list-of-integers d1, d2, d3, ... dm> where the list consists of:
    * the distances between cities (1, 2), (1, 3), ..., (1, n),
    * then the distances between cities (2, 3), (2, 4),..., (2, n)
    * etc...
    * and finally the distance between the cities (n - 1, n).

Commas `,` are used as delimitters in data-files - carriage returns, end-of-line markers, spaces, etc., should be ignored.

So, for example, the instance with 5 cities where: the city 1 is at the origin; the city 2 is 3 miles north; the city 3 is 4 miles east; the city 4 is 3 miles south; and the city 5 is 4 miles west, and all distances are the Euclidean distances between cities, is encoded as the city-file `AISearchsample.txt`:

```
NAME = AISearchsample,
SIZE = 5,
3, 4, 3, 4,
5, 6, 5,
5, 8,
5
```

With reference to the remark above, re: delimitters, the above city-file could well be presented with no carriage returns, etc., as simply

```
NAME = AISearchsample,SIZE = 5,3,4,3,4,5,6,5,5,8,5
```

## Simulated Annealing

Simulated annealing (SA) is a probabilistic technique for approximating the global optimum of a given function. Specifically, it is a meta-heuristic to approximate global optimization in a large search space for an optimization problem. It is often used when the search space is discrete (e.g., all tours that visit a given set of cities). For problems where finding an approximate global optimum is more important than finding a precise local optimum in a fixed amount of time, simulated annealing may be preferable to alternatives such as gradient descent.

The name and inspiration come from annealing in metallurgy, a technique involving heating and controlled cooling of a material to increase the size of its crystals and reduce their defects. Both are attributes of the material that depend on its thermodynamic free energy. Heating and cooling the material affects both the temperature and the thermodynamic free energy. The simulation of annealing can be used to find an approximation of a global minimum for a function with a large number of variables.

This notion of slow cooling implemented in the simulated annealing algorithm is interpreted as a slow decrease in the probability of accepting worse solutions as the solution space is explored. Accepting worse solutions is a fundamental property of meta-heuristics because it allows for a more extensive search for the global optimal solution. In general, the simulated annealing algorithms work as follows. At each time step, the algorithm randomly selects a solution close to the current one, measures its quality, and then decides to move to it or to stay with the current solution based on either one of two probabilities between which it chooses on the basis of the fact that the new solution is better or worse than the current one. During the search, the temperature is progressively decreased from an initial positive value to zero and affects the two probabilities: at each step, the probability of moving to a better new solution is either kept to 1 or is changed towards a positive value; on the other hand, the probability of moving to a worse new solution is progressively changed towards zero.

### Usage 

The SA algorithm can be carried out on any city file from the cityfiles folder (or others if they share the same format). Define the `temperature`, `cooling_rate`, and the number of `repeats` to perform.

```bash
python3 Simulated_Annealing.py cityfile temperature cooling_rate repeats
```

## Genetic Algorithm

In a genetic algorithm, a population of candidate solutions (called individuals, creatures, or phenotypes) to an optimization problem is evolved toward better solutions. Each candidate solution has a set of properties (its chromosomes or genotype) which can be mutated and altered; traditionally, solutions are represented in binary as strings of 0s and 1s, but other encodings are also possible.

The evolution usually starts from a population of randomly generated individuals, and is an iterative process, with the population in each iteration called a generation. In each generation, the fitness of every individual in the population is evaluated; the fitness is usually the value of the objective function in the optimization problem being solved. The more fit individuals are stochastically selected from the current population, and each individual's genome is modified (recombined and possibly randomly mutated) to form a new generation. The new generation of candidate solutions is then used in the next iteration of the algorithm. Commonly, the algorithm terminates when either a maximum number of generations has been produced, or a satisfactory fitness level has been reached for the population.

A typical genetic algorithm requires:
* a genetic representation of the solution domain.
* a fitness function to evaluate the solution domain.

A standard representation of each candidate solution is as an array of bits. Arrays of other types and structures can be used in essentially the same way. The main property that makes these genetic representations convenient is that their parts are easily aligned due to their fixed size, which facilitates simple crossover operations. Variable length representations may also be used, but crossover implementation is more complex in this case.

Once the genetic representation and the fitness function are defined, a GA proceeds to initialize a population of solutions and then to improve it through repetitive application of the mutation, crossover, inversion and selection operators.

### Usage

The GA can be carried out on any city file from the cityfiles folder (or others if they share the same format). Define the `population_size`, `mutation_rate`, `cut_off` number, and number of `repeats` starting with fresh populations.

```bash
python3 Genetic.py cityfile population_size mutation_rate cut_off repeats
```

